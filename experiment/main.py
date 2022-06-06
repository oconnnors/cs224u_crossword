from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import time
import json


with open('data/cryptonite-official-split/cryptonite-train.jsonl', 'r') as json_file:
    json_list = list(json_file)

input_sequences = [] 
output_sequences = []
for json_str in json_list:
    result = json.loads(json_str)
    input_sequences.append(result['clue'])
    output_sequences.append(result['answer'])


tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

# the following 2 hyperparameters are task-specific
max_source_length = 512
max_target_length = 128


# encode the inputs
task_prefix = "solve cryptic crossword:"


encoding = tokenizer(
    [task_prefix + sequence for sequence in input_sequences],
    padding="longest",
    max_length=max_source_length,
    truncation=True,
    return_tensors="pt",
)

input_ids, attention_mask = encoding.input_ids, encoding.attention_mask

# encode the targets
target_encoding = tokenizer(
    output_sequences, padding="longest", max_length=max_target_length, truncation=True
)
labels = target_encoding.input_ids

# replace padding token id's of the labels by -100 so it's ignored by the loss
labels = torch.tensor(labels)
labels[labels == tokenizer.pad_token_id] = -100

# forward pass
loss = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels).loss
loss.item()

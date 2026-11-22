import torch


with open("data/input.txt", "r", encoding="utf-8") as f:
    text = f.read()

chars = sorted(set(text))
vocab_size = len(chars)

str_to_int = {ch: i for i,ch in enumerate(chars)}
int_to_str = {i: ch for ch, i in str_to_int.items()}

def encode(s):
    return [str_to_int[c] for c in s]

def decode(ids):
    return "".join(int_to_str[i] for i in ids)

data = torch.tensor(encode(text), dtype=torch.long)




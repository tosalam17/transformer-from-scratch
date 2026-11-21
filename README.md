# transformer-from-scratch

A GPT-style transformer built from first principles in PyTorch, starting with a character-level language model on Tiny Shakespeare. Every component (tokenizer, attention, training loop) is written by hand to learn how it works, with a learning log of bugs and fixes.

> **Status:** Work in progress. Just getting started.

## Goals

- Build solid PyTorch and deep learning fundamentals by implementing a transformer without high-level libraries
- Understand every tensor shape and design choice, not just get something that runs
- Later, extend the model to quantitative finance problems (time series, cross-sectional ranking, order book data)

## Roadmap

- [ ] **Step 0:** Corpus chosen (Tiny Shakespeare), repo set up
- [ ] **Step 1:** MLP training loop written from memory (PyTorch fundamentals check)
- [ ] **Step 2:** Bigram baseline trains and samples text
- [ ] **Step 3:** Self-attention worked through on paper
- [ ] **Step 4:** Single-head self-attention
- [ ] Multi-head attention, feed-forward blocks, residuals, layer norm
- [ ] Full transformer language model
- [ ] Results and write-up

## Setup

```bash
git clone https://github.com/tosalam17/transformer-from-scratch.git
cd transformer-from-scratch
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Data

Tiny Shakespeare (about 1 MB of text from Shakespeare's plays). Details on where to get it and how it is stored: TBD.

## Results

TBD. Loss curves, sample generations, and comparisons against the bigram baseline will go here.

## Learning Log

Confusions, bugs, and fixes are tracked in `LEARNING_LOG.md`.

## References

- Vaswani et al., [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762) (2017)
- Jay Alammar, [*The Illustrated Transformer*](https://jalammar.github.io/illustrated-transformer/)
- Andrej Karpathy, [*Let's build GPT: from scratch, in code, spelled out*](https://www.youtube.com/watch?v=kCc8FmEb1nY) (used as a reference only after attempting each component)

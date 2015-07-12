# bearychat-py

A simple package for interacting with [bearychat][bc]'s API.

[bc]: http://bearychat.com

[![Build Status](https://travis-ci.org/bcho/bearychat-py.svg)](https://travis-ci.org/bcho/bearychat-py)


## Usage

### Incoming Message

```python
>>> import bearychat
>>> bearychat.Incoming('https://hook.bearychat.com').with_text('hello, world').push()
```

## Installation

```bash
pip install bearychat-py
```


## LICENSE

MIT

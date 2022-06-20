# Evmos address converter

Evmos address converter from `python3+`.

## Installation

```sh
pip install pyevmosaddressconverter
```

## Usage:

```python
from pyevmosaddressconverter import eth_to_evmos
from pyevmosaddressconverter import evmos_to_eth

eth_to_evmos('0xe7e3654bc1ea915e7216d8193ef8dd7d5dae987f')
# 'evmos1ul3k2j7pa2g4uuskmqvna7xa04w6axrl85alz5'

evmos_to_eth('evmos1ul3k2j7pa2g4uuskmqvna7xa04w6axrl85alz5')
# '0xe7e3654bc1ea915e7216d8193ef8dd7d5dae987f'
```

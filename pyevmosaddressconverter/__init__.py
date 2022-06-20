from __future__ import annotations

import binascii

from pyevmosaddressconverter.enconder.bech32 import bech32_decode
from pyevmosaddressconverter.enconder.bech32 import bech32_encode
from pyevmosaddressconverter.enconder.bech32 import convertbits
from pyevmosaddressconverter.enconder.bech32 import Encoding

EVMOS_PREFIX = 'evmos'
ETH_PREFIX = '0x'


def bech32_to_eth(wallet: str, prefix: str) -> str | None:
    decoded = bech32_decode(wallet)
    if decoded[0] != prefix:
        return None
    words = convertbits(decoded[1], 5, 8, False)
    if words is None:
        return None
    res = ''
    for w in words:
        res = f'{res}{format(w, "x").zfill(2)}'

    return f'{ETH_PREFIX}{res}'


def eth_to_bech32(wallet: str, prefix: str) -> str | None:
    splitted = wallet.split('0x')
    if len(splitted) == 2:
        raw_address = splitted[1]
    else:
        raw_address = wallet
    try:
        array = binascii.unhexlify(raw_address)
        words = [x for x in array]
        bech32_words = convertbits(words, 8, 5)
        bech32_address = bech32_encode(prefix, bech32_words, Encoding.BECH32)
    except Exception:
        return None
    if len(bech32_address) != 44:
        return None

    return bech32_address


def evmos_to_eth(wallet: str) -> str | None:
    return bech32_to_eth(wallet, EVMOS_PREFIX)


def eth_to_evmos(wallet: str) -> str | None:
    return eth_to_bech32(wallet, EVMOS_PREFIX)

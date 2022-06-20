import pytest

from pyevmosaddressconverter import eth_to_evmos
from pyevmosaddressconverter import evmos_to_eth


@pytest.mark.parametrize(
    'input, output',
    [
        ('evmos1ul3k2j7pa2g4uuskmqvna7xa04w6axrl85alz5', '0xe7e3654bc1ea915e7216d8193ef8dd7d5dae987f'),
        ('cosmos1wze8mn5nsgl9qrgazq6a92fvh7m5e6psjcx2du', None),
        ('', None),
        ('evmos1123', None),
    ],
)
def test_evmosToEth(input, output):
    assert evmos_to_eth(input) == output


@pytest.mark.parametrize(
    'input, output',
    [
        ('0xe7e3654bc1ea915e7216d8193ef8dd7d5dae987f', 'evmos1ul3k2j7pa2g4uuskmqvna7xa04w6axrl85alz5'),
        ('cosmos1wze8mn5nsgl9qrgazq6a92fvh7m5e6psjcx2du', None),
        ('evmos1ul3k2j7pa2g4uuskmqvna7xa04w6axrl85alz5', None),
        ('', None),
    ],
)
def test_ethToEvmos(input, output):
    assert eth_to_evmos(input) == output

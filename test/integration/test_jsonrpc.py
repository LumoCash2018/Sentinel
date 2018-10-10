import pytest
import sys
import os
import re
os.environ['SENTINEL_ENV'] = 'test'
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import config

from lumocashd import LumoCashDaemon
from lumocash_config import LumoCashConfig


def test_lumocashd():
    config_text = LumoCashConfig.slurp_config_file(config.lumocash_conf)
    network = 'mainnet'
    is_testnet = False
    genesis_hash = u'00000bbf403e648b97c0bf067fcb24bbd7123a00085f4cbdc811432ce5f46ecd'
    for line in config_text.split("\n"):
        if line.startswith('testnet=1'):
            network = 'testnet'
            is_testnet = True
            genesis_hash = u'00000043a2ccde9852361c394d3df73f3404983c0a3f6e91ef0b595a0beb047a'

    creds = LumoCashConfig.get_rpc_creds(config_text, network)
    lumocashd = LumoCashDaemon(**creds)
    assert lumocashd.rpc_command is not None

    assert hasattr(lumocashd, 'rpc_connection')

    # LumoCash testnet block 0 hash == 00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c
    # test commands without arguments
    info = lumocashd.rpc_command('getinfo')
    info_keys = [
        'blocks',
        'connections',
        'difficulty',
        'errors',
        'protocolversion',
        'proxy',
        'testnet',
        'timeoffset',
        'version',
    ]
    for key in info_keys:
        assert key in info
    assert info['testnet'] is is_testnet

    # test commands with args
    assert lumocashd.rpc_command('getblockhash', 0) == genesis_hash

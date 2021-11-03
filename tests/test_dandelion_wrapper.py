# test_dandelion_wrapper.py

from dandelion.dandelion_api import DandelionClient


def test_client_creation():
    dc = DandelionClient()
    assert DandelionClient is not None
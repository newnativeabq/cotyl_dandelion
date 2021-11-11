# test_dandelion_wrapper.py

from dandelion.dandelion_api import DandelionClient

import logging
logger = logging.getLogger(__name__)



def test_client_creation():
    dc = DandelionClient()
    assert DandelionClient is not None


def test_client_up():
    dc = DandelionClient()
    assert dc.up == True, f'client not up. {dc.networks}'


def test_client_get():
    dc = DandelionClient()
    query = {"query": "query cardanoDbSyncProgress {cardanoDbMeta (initialized syncPercentage}}}"}
    resp = dc.post(data = query)
    logger.warning(resp.content)
    assert 1 == 0


            # query = {"query": "query cardanoDbSyncProgress {cardanoDbMeta (initialized syncPercentage}}}"}
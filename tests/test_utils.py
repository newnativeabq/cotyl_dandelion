# test_utils.py


from dandelion.utils import ping

import logging
logger = logging.getLogger(__name__)

def test_ping():
    res = ping('https://www.a_hopefully_unknon_site.com')
    logger.info(res)
    res = ping('google.com')
    logger.info(res)
    assert len(res) > 0
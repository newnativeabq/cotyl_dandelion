"""
Scratch Paper
"""



from dandelion.dandelion_api import DandelionClient

import json


def run():
    dc = DandelionClient()
    query = {"query": "query cardanoDbSyncProgress {cardanoDbMeta (initialized syncPercentage}}}"}
    rep = dc.post(data=query)

    print(rep.content)
    return rep




if __name__ == '__main__':
    run()
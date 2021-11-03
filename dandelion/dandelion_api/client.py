# client.py

"""
Client

Dandelion Client Main Object
"""

from .sync import SyncService



class SimpleAPIClient():
    def __init__(self, service_sync: SyncService) -> None:
        self.service_sync = service_sync


    @property
    def up(self):
        summaries = [sync['available'] for sync in self.networks]
        return len(summaries) == sum(summaries)
    

    @property
    def networks(self):
        return self.service_sync.all_networks


class DandelionClient(SimpleAPIClient):

    def __init__(self, network: str = 'testnet') -> None:
        super().__init__(service_sync=SyncService(network=network))
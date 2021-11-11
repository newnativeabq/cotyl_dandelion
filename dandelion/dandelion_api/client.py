# client.py

"""
Client

Dandelion Client Main Object
"""

from .sync import SyncService
from dandelion.utils import pretty_print_post

import requests


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

    def __init__(self, network: str = 'testnet', api='graphql') -> None:
        super().__init__(service_sync=SyncService(network=network))

        self.api = api
        self.network = network
        self._host = None


    @property
    def host(self):
        if self._host is None:
            sync = self.service_sync[self.api]
            self._host = sync['protocol'] + sync['host']
        return self._host


    def get(self, *args, **kwargs) -> requests.Response:
        # Get a fresh sync
        sync = self.service_sync.graphql
        # Pull the headers and availability
        headers = sync['header']
        assert sync['available'], f"Network not available. {sync}"

        r = requests.Request(
            'GET',
            url=self.host, 
            headers=headers,
            *args, **kwargs)

        with requests.Session() as session:
            return session.send(r.prepare())

    
    def post(self, *args, **kwargs) -> requests.Response:
        # Get a fresh sync
        sync = self.service_sync.graphql
        # Pull the headers and availability
        headers = sync['header']
        assert sync['available'], f"Network not available. {sync}"

        r = requests.Request(
            'POST',
            url=self.host, 
            headers=headers,
            *args, **kwargs)

        print(pretty_print_post(r.prepare()))

        with requests.Session() as session:
            return session.send(r.prepare())
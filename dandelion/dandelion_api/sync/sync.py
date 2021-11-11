# sync.py

"""
Sync

Sync with Dandelion network(s) and get access information
"""


from dandelion.utils import ping



class SyncService():
    
    def __init__(self, network: str) -> None:
        self.network = network
        assert network in ['testnet', 'mainnet']

    
    @property
    def all_networks(self):
        syncs = [
            self.graphql,
            self.postgres,
        ]
        return syncs

    
    @property
    def graphql(self):
        sync = {
            'host': f'graphql-api.{self.network}.dandelion.link',  ## Works until multi-domain/service
            'header': {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            'protocol': 'http://'
        }
        return self.check_available(sync)

    
    @property
    def postgres(self):
        sync = {
            'host': f'postgrest-api.{self.network}.dandelion.link',
            'header': {
                'Content-Type': 'application/json',
            },
            'protocol': 'http://'
        }
        return self.check_available(sync)

    
    def __getitem__(self, key):
        return getattr(self, key)


    def check_available(self, sync):
        sync = self.ping(sync)
        sync['available'] = sync['ping']['status'] == 'up'
        return sync

    
    def ping(self, sync):
        host = sync['host']
        response = ping(host)

        if response.__contains__('0%'):
            status = 'up'
        else:
            status = 'down'

        sync['ping'] = {
            'res': response,
            'status': status,
        }
        return sync

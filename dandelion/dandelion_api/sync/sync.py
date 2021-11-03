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
            self.graphql_api,
            self.postgres_api,
        ]
        return syncs

    
    @property
    def graphql_api(self):
        sync = {
            'uri': f'graphql-api.{self.network}.dandelion.link',  ## Works until multi-domain/service
            'header': {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
        }
        return self.check_available(sync)

    
    @property
    def postgres_api(self):
        sync = {
            'uri': f'postgrest-api.{self.network}.dandelion.link',
            'header': {
                'Content-Type': 'application/json',
            },
        }
        return self.check_available(sync)


    def check_available(self, sync):
        sync = self.ping(sync)
        sync['available'] = sync['ping']['status'] == 'up'
        return sync

    
    def ping(self, sync):
        host = sync['uri']
        print('imp ping getting', host)
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

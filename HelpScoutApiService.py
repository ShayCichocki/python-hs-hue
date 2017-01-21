import requests
from requests.auth import HTTPBasicAuth


class HelpScoutApiService(object):
    api_key = ''

    def __init__(self, api_key = ''):
        self.api_key = api_key
        pass

    def get_mine_folder_in_mailbox(self, mailbox_id):
        folders_response = requests.get('https://api.helpscout.net/v1/mailboxes/%s/folders.json' % mailbox_id,
                         auth=HTTPBasicAuth(self.api_key, 'X'))

        if folders_response.status_code != 200:
            return None

        _folders = folders_response.json()
        _folder_items = _folders['items']

        for item in _folder_items:
            if item['name'] == 'Mine':
                return item

        return None
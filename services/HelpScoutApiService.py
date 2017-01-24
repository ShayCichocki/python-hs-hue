import requests
from requests.auth import HTTPBasicAuth


class HelpScoutApiService(object):
    api_key = ''

    def __init__(self, api_key=''):
        self.api_key = api_key
        pass

    def get_mine_folder_in_mailbox(self, mailbox_id):
        return self.get_folder_by_name_in_mailbox(mailbox_id, 'Mine')

    def get_conversations_in_folder(self, mailbox_id, folder_id):
        """
        https://api.helpscout.net/v1/mailboxes/{mailboxId}/folders/{folderId}/conversations.json

        :param mailbox_id: int
        :param folder_id: int
        """
        url = 'https://api.helpscout.net/v1/mailboxes/{mailbox_id}/folders/{folder_id}/conversations.json'.format(
            mailbox_id=mailbox_id, folder_id=folder_id)

        conversation_response = requests.get(url, auth=HTTPBasicAuth(self.api_key, 'X'))
        _conversations = conversation_response.json()
        return _conversations['items']

    def get_folder_by_name_in_mailbox(self, mailbox_id, folder_name="Mine"):
        folders_response = requests.get('https://api.helpscout.net/v1/mailboxes/%s/folders.json' % mailbox_id,
                                        auth=HTTPBasicAuth(self.api_key, 'X'))

        if folders_response.status_code != 200:
            return None

        _folders = folders_response.json()
        _folder_items = _folders['items']

        for item in _folder_items:
            if item['name'] == folder_name:
                return item
        return None

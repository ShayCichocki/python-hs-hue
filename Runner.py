import threading
from ConfigParser import SafeConfigParser

from HelpScoutApiService import HelpScoutApiService
from HueInterfaceService import HueInterfaceService

from entities import Color

config = SafeConfigParser()
config.read('config.ini')
userId = config.get('main', 'un')
ip_address = config.get('main', 'ip')
api_key = config.get('hs', 'api_key')
mailbox_id = config.get('hs', 'mailbox_id')

hue_service = HueInterfaceService(ip_address, userId)
hs_api_service = HelpScoutApiService(api_key)


def check_service():
    mine_folder = hs_api_service.get_mine_folder_in_mailbox(mailbox_id)
    if mine_folder['activeCount'] > 0:
        hue_service.change_color(1, Color.COLOR_RED)
    else:
        hue_service.change_color(1, Color.COLOR_WHITE)

    t = threading.Timer(10, check_service)
    t.start()


check_service()

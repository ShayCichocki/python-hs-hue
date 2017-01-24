import threading
from ConfigParser import SafeConfigParser

from services.HelpScoutApiService import HelpScoutApiService
from services.HueInterfaceService import HueInterfaceService
from services.QueueNotifierService import QueueNotifierService

config = SafeConfigParser()
config.read('config.ini')
user_id = config.get('main', 'un')
ip_address = config.get('main', 'ip')
api_key = config.get('hs', 'api_key')
mailbox_id = config.get('hs', 'mailbox_id')

hue_service = HueInterfaceService(ip_address, user_id)
hs_api_service = HelpScoutApiService(api_key)
queue_notifier = QueueNotifierService(api_key, mailbox_id, hue_service, hs_api_service)


def check_service():
    queue_notifier.check_queue()

    t = threading.Timer(10, check_service)
    t.start()

check_service()

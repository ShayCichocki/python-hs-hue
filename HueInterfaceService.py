import requests
import json

class HueInterfaceService(object):
    ip_address = ''
    user_id = ''

    def __init__(self, ip_address, user_id):
        """

        :type user_id: str
        :type ip_address: str
        """
        self.ip_address = ip_address
        self.user_id = user_id

    def change_color(self, light_id, color):
        """
        :param light_id: int
        :type color: Color
        """
        put_lights_uri = '%s/api/%s/lights/%s/state' % (self.ip_address, self.user_id, light_id)
        requests.put(put_lights_uri, json.dumps(color.to_state_json()))

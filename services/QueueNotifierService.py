from entities import Color


class QueueNotifierService(object):
    last_count = 0
    current_color = Color.COLOR_WHITE
    api_key = ''
    mailbox_id = ''

    def __init__(self, api_key='', mailbox_id='', hue_service=None, hs_api_service=None):
        self.api_key = api_key
        self.mailbox_id = mailbox_id
        self.hue_service = hue_service
        self.hs_api_service = hs_api_service
        pass

    def check_queue(self):
        mine_folder = self.hs_api_service.get_mine_folder_in_mailbox(self.mailbox_id)
        if mine_folder['activeCount'] > 0:
            self.do_has_items(mine_folder['activeCount'])
        else:
            self.last_count = 0
            self.current_color = Color.COLOR_WHITE

        self.hue_service.change_color(1, self.current_color)

    def do_has_items(self, new_active_count):
        if new_active_count != self.last_count:
            color = Color.COLOR_GREEN
            conversations = self.hs_api_service.get_conversations_in_folder(self.mailbox_id, folder_id=445631)
            for conversation in conversations:
                if conversation['tags'] and 'vip' in conversation['tags']:
                    color = Color.COLOR_RED
                elif conversation['subject'] and 'workflow' in conversation['subject']:
                    color = Color.COLOR_BLUE
            self.last_count = new_active_count
            self.current_color = color

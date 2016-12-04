from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from pymongo import MongoClient


class Thumbot:

    THUMBS_UP_EMOJI = '\U0001F44D'
    THUMBS_DOWN_EMOJI = '\U0001F44E'

    def __init__(self):
        client = MongoClient()
        self.db = client.thumbot

        self.ups = []
        self.downs = []

    @property
    def up_label(self):
        if self.ups:
            return '{} {}'.format(self.THUMBS_UP_EMOJI, len(self.ups))

        return self.THUMBS_UP_EMOJI

    @property
    def down_label(self):
        if self.downs:
            return '{} {}'.format(self.THUMBS_DOWN_EMOJI, len(self.downs))

        return self.THUMBS_DOWN_EMOJI

    def _create_button(self, label, callback):
        return InlineKeyboardButton(label, callback_data=callback)

    def _create_keyboard(self, *buttons):
        keyboard = InlineKeyboardMarkup()

        return keyboard.row(*buttons)

    def keyboard(self, up_label=None, down_label=None):
        up_button = self._create_button(self.up_label, 'thumb_up')
        down_button = self._create_button(self.down_label, 'thumb_down')
        return self._create_keyboard(up_button, down_button)

    def check(self, message):
        # I'm sure that there is a better way to do this function
        self.chat_id = message.from_user.id
        self.message_id = message.message_id

        message = self.db.messages.find_one({
            'chat_id': self.chat_id,
            'message_id': self.message_id,
        })

        if not message:
            object_id = self.db.messages.insert_one({
                'chat_id': self.chat_id,
                'message_id': self.message_id,
                'ups': self.ups,
                'downs': self.downs,
            }).inserted_id

            message = self.db.messages.find_one({'_id': object_id})

        self.ups = message['ups']
        self.downs = message['downs']

    def update(self):
        self.db.messages.update_one(
            {
                'chat_id': self.chat_id,
                'message_id': self.message_id,
            },
            {
                '$set': {
                    'ups': self.ups,
                    'downs': self.downs
                }
            }
        )

    def add_thumb_up(self, user_id):
        if user_id in self.ups:
            return False

        self.ups.append(user_id)
        if user_id in self.downs:
            self.downs.remove(user_id)

        self.update()
        return True

    def add_thumb_down(self, user_id):
        if user_id in self.downs:
            return False

        self.downs.append(user_id)
        if user_id in self.ups:
            self.ups.remove(user_id)
        self.update()

        return True

    def reset(self):
        self.chat_id = self.message_id = ''
        self.ups = []
        self.downs = []

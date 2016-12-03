from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from pymongo import MongoClient


client = MongoClient()
db = client.messages


class Thumbot:

    THUMBS_UP_EMOJI = '\U0001F44D'
    THUMBS_DOWN_EMOJI = '\U0001F44E'

    @property
    def up_label(self):
        if self.ups:
            return '{} {}'.format(self.THUMBS_UP_EMOJI, self.ups)

        return self.THUMBS_UP_EMOJI

    @property
    def down_label(self):
        if self.downs:
            return '{} {}'.format(self.THUMBS_DOWN_EMOJI, self.downs)

        return self.THUMBS_DOWN_EMOJI

    def _create_button(self, label, callback):
        return InlineKeyboardButton(label, callback_data=callback)

    def _create_keyboard(self, *buttons):
        keyboard = InlineKeyboardMarkup()

        return keyboard.row(*buttons)

    def keyboard(self):
        up_button = self._create_button(self.up_label, 'ups')
        down_button = self._create_button(self.down_label, 'downs')
        return self._create_keyboard(up_button, down_button)

    def check(self, message):
        # I'm sure that there is a better way to do this function
        self.chat_id = message.from_user.id
        self.message_id = message.message_id

        message = db.find_one({
            'chat_id': self.chat_id,
            'message_id': self.message_id,
        })

        if not message:
            object_id = db.insert_one({
                'chat_id': self.chat_id,
                'message_id': self.message_id,
                'ups': [],
                'downs': [],
            }).inserted_id

            message = db.find_one({'_id': object_id})

        self.ups = message['ups']
        self.downs = message['downs']

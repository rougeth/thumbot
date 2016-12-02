from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class Keyboard:

    THUMBS_UP_EMOJI = '\U0001F44D'
    THUMBS_DOWN_EMOJI = '\U0001F44E'

    def __init__(self, ups=0, downs=0):
        self.ups = ups
        self.downs = downs

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

    def generate(self):
        up_button = self._create_button(self.up_label, 'ups')
        down_button = self._create_button(self.down_label, 'downs')
        return self._create_keyboard(up_button, down_button)

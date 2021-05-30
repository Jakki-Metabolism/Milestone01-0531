import time
import telepot
from telepot.loop import MessageLoop
from telepot.delegate import pave_event_space, per_chat_id, create_open
from telepot.namedtuple import ReplyKeyboardMarkup

keyboard_content = [['Calculate the calories intake by photo'],
                    ['Calculate the calories intake by text'],
                    ['Calculate the calories in exercise'],
                    ['Recommend exercise video']]
class JakkiBot(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(JakkiBot, self).__init__(*args, **kwargs)
        self.indicator = 'choose_function'

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if self.indicator == 'choose_function':
            mark_up = ReplyKeyboardMarkup(keyboard=keyboard_content,
                                          one_time_keyboard=True)
            bot.sendMessage(chat_id, text='What can I help you?', reply_markup=mark_up)
            self.indicator = 'function_input'
        elif self.indicator == 'function_input':
            if msg['text'] == 'Calculate the calories intake by photo' or 'Calculate the calories intake by text':
                bot.sendMessage(chat_id, text='Photo/Text received')
            else:
                bot.sendMessage(chat_id, 'Sure!')
            self.indicator = 'choose_function'


TOKEN = '1865792707:AAFenT5wu6D5iMFvApvjXGiRMHQJ5ti7WSs'

bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, JakkiBot, timeout=10),
])
MessageLoop(bot).run_as_thread()

while 1:
    time.sleep(100)
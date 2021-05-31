import time
import telepot
from telepot.loop import MessageLoop
from telepot.delegate import pave_event_space, per_chat_id, create_open
from telepot.namedtuple import ReplyKeyboardMarkup

keyboard_content = [['See my body data'],
                    ['Add a food diary'],
                    ['See my food diary'],
                    ['Add an exercise record'],
                    ['Get a exercise video']]
class JakkiBot(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(JakkiBot, self).__init__(*args, **kwargs)
        self.indicator = 'choose_function'

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if self.indicator == 'choose_function':
            mark_up = ReplyKeyboardMarkup(keyboard=keyboard_content,
                                          one_time_keyboard=True)
            bot.sendMessage(chat_id, "Hi, I'm your health manager FitNote! What may I help you?",
                            reply_markup=mark_up)
            self.indicator = 'second_layer'
        elif self.indicator == 'second_layer':
            if msg['text'] == 'See my body data':
                mark_up02 = ReplyKeyboardMarkup(keyboard=[['Edit my data'],
                                                          ['Calculate my BMI']],
                                                one_time_keyboard=True)
                bot.sendMessage(chat_id, "Name: Test\n"
                                         "Weight: 50 kg\n"
                                         "Height: 160 cm\n"
                                         "Last Update: 2021-05-29\n",reply_markup=mark_up02)
                self.indicator = 'second_layer_01'
            elif msg['text'] == 'Add a food diary':
                bot.sendMessage(chat_id, "Please send me your food diary in the format of: year-mm-dd num calories")
                self.indicator = 'second_layer_02'
            elif msg['text'] =='See my food diary':
                bot.sendMessage(chat_id, "Below is your food diary\n"
                                         "2021-05-20 01 200 calories\n"
                                         "2021-05-20 02 500 calories\n"
                                         "2021-05-31 01 200 calories\n")
                self.indicator = 'choose_function'
            elif msg['text'] =='Add an exercise record':
                bot.sendMessage(chat_id, "Please send me your exercise record in the format of: xxxx-xx-xx exercise_name time(min)")
                self.indicator = 'second_layer_04'
            elif msg['text'] == 'Get a exercise video':
                bot.sendMessage(chat_id, "Below is a video recommended for you!")
                bot.sendMessage(chat_id, 'https://youtu.be/1piFN_ioMVI')
                self.indicator = 'choose_function'
            else:
                bot.sendMessage(chat_id, 'Cannot understand, please restart!')
        elif self.indicator == 'second_layer_01':
            if msg['text'] == 'Calculate my BMI':
                bot.sendMessage(chat_id, 'Your BMI is 19.5!')
            self.indicator = 'choose_function'
        else:
            bot.sendMessage(chat_id, "Successful Noted")
            self.indicator = 'choose_function'


TOKEN = '1865792707:AAFenT5wu6D5iMFvApvjXGiRMHQJ5ti7WSs'

bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, JakkiBot, timeout=500),
])
MessageLoop(bot).run_as_thread()

while 1:
    time.sleep(100)
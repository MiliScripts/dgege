#___________________________imports_________________________________
import yaml
from pykeyboard import InlineButton , InlineKeyboard


#____________________________configs________________________________
with open('configs/config.yml' , encoding='UTF-8') as f :
    bot_data = yaml.safe_load(f)

bot_token = bot_data['BOT_TOKEN']
api_id = bot_data['API_ID']
api_hash = bot_data['API_HASH']
admins = bot_data['ADMINS']
owner = bot_data['OWNER']
mongo_string  = bot_data['MONGO_DB']
panel_url = bot_data['PANEL_URL']
panel_username = bot_data['PANEL_USERNAME']
panel_password = bot_data['PANEL_PASSWORD']


#____________________________msgs________________________________
with open('configs/messages.yml', encoding='UTF-8') as f :
    bot_messages = yaml.safe_load(f)

start_message = bot_messages['START']
ask_username_message = bot_messages['ASK_USERNAME']
ask_traffic_message = bot_messages['ASK_TRAFFIC']
ask_expire_days_message = bot_messages['ASK_EXPIRE']
creation_success_response = bot_messages['SUCCESS']
creation_fail_response = bot_messages['FAILED']  



#____________________________keyboards____________________________
#main-start kb_______________________
main_kb = InlineKeyboard(row_width=2)
main_kb.add(
    InlineButton('+ ساخت کاربر', 'main:create'),
    InlineButton('- حذف کاربر', 'main:remove'),
    InlineButton(' تمدید کاربر', 'main:extent'),
    InlineButton('دیدن کاربران', 'main:users'),
)
#choose traffic________________________
traffic_kb = InlineKeyboard(row_width=3)
traffic_kb.add(
    InlineButton("نامحدود", 'traffic:30'),
)
traffic_kb.add(
    InlineButton("20 GB", 'traffic:20'),
    InlineButton("40 GB", 'traffic:40'),
    InlineButton("60 GB", 'traffic:60'),
    InlineButton("100 GB", 'traffic:100'),
    InlineButton("120 GB", 'traffic:120'),
    InlineButton("200 GB", 'traffic:200'),
    InlineButton("لغو", 'cancell'),
    
)
#choose expire___________________________
expire_days_kb = InlineKeyboard(row_width=2)
expire_days_kb.add(
    InlineButton('1 ماهه','days:30'),
    InlineButton('2 ماهه','days:60'),
    InlineButton('3 ماهه','days:90'),
    InlineButton('4 ماهه','days:120'),
    InlineButton("لغو", 'cancell'), 
)



confirm_kb= InlineKeyboard(row_width=1)
confirm_kb.add(
    InlineButton('تایید','confirm-creation'),
    InlineButton("لغو", 'cancell')
    
)
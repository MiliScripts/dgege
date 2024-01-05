#_______________imports___________________
from pyrogram import Client ,idle,filters
from configs.config import *
import requests
from asyncio import get_event_loop
#_______________client define______________
admin_bot = Client(name ='admin_mili_vpn_bot',
                   api_id=api_id,
                   api_hash=api_hash,
                   bot_token=bot_token)


admins_step = {}




@admin_bot.on_message(filters.text)
async def message_handler(c,m):
    
    message_sender = m.chat.id
    if message_sender not in admins_step:
        admins_step[message_sender] = {
            'name':'',
            'traffic':'',
            'expire_days' : '',
            'step' : ''
        }
    message_text = m.text
    if message_sender not in admins:
        print('NOt Authenticated Admin [X]')
        return 
    
    if message_text=='/start':
        await m.reply(text=start_message,reply_markup=main_kb)
    elif admins_step[message_sender]['step']=='create-name':
        admins_step[message_sender]['name'] = message_text
        print('username selected as [{}]'.format(message_text))
        await admin_bot.delete_messages(chat_id=m.chat.id,message_ids=[m.id,m.id-1])
        await m.reply(text=ask_traffic_message,reply_markup=traffic_kb)
        
        

def create_user(name,traffic,expire_days):
    url = 'https://sub.emamdad.site/api/user/create'
    data = {
        "username": name,
        "panel_domain" : "b2",
        "inbound_id" : "1",
        "flag":"🇩🇪",
        "traffic":int(traffic),
        "expire_days":int(expire_days)
    }
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    sub_link = response.json()['subscription_link']
    print(response.json())
    return sub_link



#handle inlime=ne buttons
@admin_bot.on_callback_query()
async def handle_buttons(c,q):
    print('user id : {}'.format(q.message.chat.id))
    print(type(q.message.chat.id))
    print(admins)
    sender =  q.message.chat.id
    if q.message.chat.id not in admins:
        return 
    if q.message.chat.id not in admins_step:
        admins_step[q.message.chat.id] = {
            'name':'',
            'traffic':'',
            'expire_days' : '',
            'step' : ''
        }
    if q.data.split(':')[0]=='main':
        command = q.data.split(':')[1]
        print('[+] {} selection'.format(command))
        if command=='create':
            print('[+] creating new user')
            await q.edit_message_text('اسم کاربر را وارد کنید')
            admins_step[q.message.chat.id]['step'] = 'create-name'
        elif command=='remove':
            print('[+] removing user')
        elif command=='extent':
            print('[+] extentning user')
        elif command=='users':
            print('[+] checking user list')
    elif q.data.split(':')[0]=='traffic':
        print('[+] traffic selection ')
        
        selected_traffic = q.data.split(':')[1]
        admins_step[q.message.chat.id]['traffic'] = selected_traffic
        await q.edit_message_text(text=ask_expire_days_message,reply_markup=expire_days_kb)
        print(admins_step)
    elif q.data.split(':')[0]=='days':
        print('[+] days selection ')
        selected_days = q.data.split(':')[1]
        admins_step[q.message.chat.id]['expire_days'] = selected_days
        print(admins_step)
        await q.edit_message_text(text='آیا از ساخت کاربر اطمیمنان دارید ؟ ',reply_markup=confirm_kb)
    elif q.data=='cancell':
        admins_step[q.message.chat.id]= {
            'name':'',
            'traffic':'',
            'expire_days' : '',
            'step' : ''
        }
        await q.edit_message_text('عملیات لغو شد')    
    elif q.data=='confirm-creation':
        print('user creation cinfirmed')    
        await q.edit_message_text('[*] درحال ساخت کابر لطفا صبر کنید')
        name = admins_step[sender]['name']
        traffic = admins_step[sender]['traffic']
        expire_days =admins_step[sender]['expire_days']
        sub = create_user(name=name,expire_days=expire_days,traffic=traffic)
        await q.edit_message_text(sub)
    




async def main():
    await admin_bot.start()
    print('[*] Bot Started')
    await idle()
    await admin_bot.stop()
    
    
    
loop = get_event_loop()
loop.run_until_complete(main())
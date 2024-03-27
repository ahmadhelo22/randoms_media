from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, CallbackQuery
import os
import requests
import random
from text_for_bot import about_the_bot, start_the_bot, suggestions, the_bots, the_user_helper
from Scheduling_web import buffer, metricool
from data import read, write 
from buttoms_replay import *
from button_replay_ai import *

# تجهيز قاعده البيانات لاضافع ال id 
db_path = 'db.json'
if os.path.exists(db_path):
    pass
else:
    write(db_path, [])
data = read(db_path)
 
bot_token="6947038177:AAHxy7DESCDmegAH72Cnu4I3ikP4643SXfc"
#معلومات و التعريف عن البوت
bot_pyrogram = Client(
    name='Bot',
    api_hash="db93b5d1b9cc15b7b8512a7082a99692",
    api_id=29817603,
    bot_token=bot_token
)

#مولد لنكات الصفحات
async def link_buttom_for_accounts(msg, link, app_name):
        
    k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS",url=f"{link}")]])
    await msg.reply_text(f"شاهد كل جديد على {app_name}",reply_markup=k,disable_web_page_preview=True)		


def read_text(file_path):
        # افتح ملف التي اكس تي للقراءة
    with open(file_path, 'r') as file:
        # اقرأ المحتوى واحفظه في متغير
        content = file.read()

        return content
#########################################################
#########################################################

#اوامر المستخدم معرفه عدد المستخدمين
@bot_pyrogram.on_message(filters.command('users_num'))
async def on_owner_command(bot:Client, msg:Message):

    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    if user_id == 5497992601 :
        users_count = len(data)
        await msg.reply(users_count)

# معرفه id المستخدمين اوامر المستخدم
@bot_pyrogram.on_message(filters.command('users_id'))
async def on_owner_command(bot:Client, msg:Message):

    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    if user_id == 5497992601 :
        for i in data:
            await msg.reply(i)

#اوامر المستخدم معرفه معلومات حول مستخدم واحد فقط
@bot_pyrogram.on_message(filters.command('user'))
async def on_owner_command(bot:Client, msg:Message):

    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    if user_id == 5497992601 :
        try:
            id = msg.text
            name = id.split(None, 1)[1]
            info = await bot.get_chat(int(name))
            await msg.reply(info)
        except:
            await msg.reply('اختر ال id الذي تود البحث عنه')

#اوامر المستخدم ارسال نص لكل مستخدمين البوت
@bot_pyrogram.on_message(filters.command('user_bc'))
async def on_owner_command(bot:Client, msg:Message):

    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    if user_id == 5497992601 :
        try:
            id = msg.text
            text_to_send = id.split(None, 1)[1]
            for i in data:
                    await bot.send_message(i, text_to_send)
        except:
            await msg.reply("يوجد مشكله بارسال الرسائل لجميع المستخدمين او يجب ان تكتب الرساله التي تود ارسالها للمستخدمين")

# ارسال ملف يحتوي على الid الخاص بكل المستخدمين 
@bot_pyrogram.on_message(filters.command('users_file'))
async def on_owner_command(bot:Client, msg:Message):

    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    if user_id == 5497992601 :
        await bot.send_document(user_id, 'db.json')

# help, uh, user_help اوامر المستخدم
@bot_pyrogram.on_message(filters.command(['help', 'user_help', 'uh']))
async def on_owner_command(bot:Client, msg:Message):

    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    if user_id == 5497992601 :
        text = the_user_helper()
        await msg.reply(text)

#########################################################
#########################################################
        


#  بدايه البوت و الامر  'start'
@bot_pyrogram.on_message(filters.command('start'))
async def start(bot:Client, msg:Message):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    #حفظ id المستخدم فقط اذا ضغط ستارت start 
    if user_id not in data:
        data.append(user_id)
        write(db_path, data)
    
    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"

    req = requests.get(url)
    
    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:


        #الرد بالازرار
        buttoms = buttoms_replay()
        replay_markup = ReplyKeyboardMarkup(buttoms, one_time_keyboard= True, resize_keyboard=True)

        text = start_the_bot()

        # ارسال الرساله الترحيبيه
        await bot.send_message(user_id, text, reply_markup=replay_markup)

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		


@bot_pyrogram.on_message(filters.regex('صفحاتنا'))
async def pages_(bot:Client, msg):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    #حفظ id المستخدم فقط اذا ضغط ستارت start 
    if user_id not in data:
        data.append(user_id)
        write(db_path, data)

    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        #الرد بالازرار
        buttoms = pages()
        replay_markup = ReplyKeyboardMarkup(buttoms, one_time_keyboard= True, resize_keyboard=True)

        # ارسال الرساله الترحيبيه
        await bot.send_message(user_id, "تابعنا على وسائل التواصل الاجتماعي", reply_markup=replay_markup)

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		

@bot_pyrogram.on_message(filters.regex('بوتاتنا'))
async def pages_(bot:Client, msg):

        #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    #حفظ id المستخدم فقط اذا ضغط ستارت start 
    if user_id not in data:
        data.append(user_id)
        write(db_path, data)

    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:

        k = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"RANDOMS_pc",url=f"https://t.me/RANDOMS1_bot")
                ],
                [
                    InlineKeyboardButton(f"RANDOMS_book",url=f"https://t.me/RANDOMS_book_bot")
                ]
            ]
            )
        # ارسال الرساله 
        await bot.send_message(user_id, the_bots(), reply_markup=k, disable_web_page_preview=True)

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		

@bot_pyrogram.on_message(filters.regex('حول البوت'))
async def pages_(bot:Client, msg:Message):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    #حفظ id المستخدم فقط اذا ضغط ستارت start 
    if user_id not in data:
        data.append(user_id)
        write(db_path, data)

        # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        # ارسال الرساله الترحيبيه

        k = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"TELEGRAM",url=f"https://t.me/ahmad0alhelo")
                ],
                [
                    InlineKeyboardButton(f"INSTAGRAM",url=f"https://www.instagram.com/ahmad.alhelok/?hl=ar")
                ],
                [
                    InlineKeyboardButton(f'FACEBOOK', url='https://www.facebook.com/ahmad.alhel0')
                ]
            ]
            )

        await msg.reply_text(about_the_bot(),reply_markup=k,disable_web_page_preview=True)		


    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		

#للتواصل معي بخصوص البوت
@bot_pyrogram.on_message(filters.regex('لاي اقتراحات'))
async def pages_(bot:Client, msg:Message):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    #حفظ id المستخدم فقط اذا ضغط ستارت start 
    if user_id not in data:
        data.append(user_id)
        write(db_path, data)

        # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        # ارسال الرساله الترحيبيه

        k = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"TELEGRAM",url=f"https://t.me/ahmad0alhelo")
                ],
                [
                    InlineKeyboardButton(f"INSTAGRAM",url=f"https://www.instagram.com/ahmad.alhelok/?hl=ar")
                ],
                [
                    InlineKeyboardButton(f'FACEBOOK', url='https://www.facebook.com/ahmad.alhel0')
                ]
            ]
            )

        await msg.reply_text(suggestions(),reply_markup=k,disable_web_page_preview=True)		


    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		


#للتواصل معي بخصوص البوت
@bot_pyrogram.on_message(filters.regex('مواقع لجدوله المنشورات'))
async def pages_(bot:Client, msg:Message):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    #حفظ id المستخدم فقط اذا ضغط ستارت start 
    if user_id not in data:
        data.append(user_id)
        write(db_path, data)

        # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:

        text = '''افضل المواقع لجدوله المنشورات '''

        k = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(f"buffer", callback_data='buffer')
                    ],
                    [
                        InlineKeyboardButton(f"metricool", callback_data='metricool')
                    ]
                ]
            )
        await msg.reply_text(text,reply_markup=k,disable_web_page_preview=True)		


    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		

#للتواصل معي بخصوص البوت
@bot_pyrogram.on_message(filters.regex('مواقع ذكاء اصطناعي'))
async def pages_(bot:Client, msg:Message):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    #حفظ id المستخدم فقط اذا ضغط ستارت start 
    if user_id not in data:
        data.append(user_id)
        write(db_path, data)

        # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:

        text = '''افضل مواقع الذكاء الاصطناعي 
        معظم المواقع تحتاج vpn'''

        k = ai_web(InlineKeyboardMarkup, InlineKeyboardButton)
        await msg.reply_text(text,reply_markup=k,disable_web_page_preview=True)	

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		
	
@bot_pyrogram.on_callback_query (filters.regex('remove_bg'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :
    k = remove_bg(InlineKeyboardMarkup, InlineKeyboardButton)
    text = 'افضل مواقع الذكاء الاصطناعي لازالة خلفيه الصور'
    await query.edit_message_text(text, reply_markup = k)

@bot_pyrogram.on_callback_query (filters.regex('photo_up_scaler'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :
    k = photo_up_scaler(InlineKeyboardMarkup, InlineKeyboardButton)
    text = 'افضل مواقع الذكاء الاصطناعي لتحسين جوده الصوره'
    await query.edit_message_text(text, reply_markup = k)

@bot_pyrogram.on_callback_query (filters.regex('photo_Compression'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :
    k = photo_Compression(InlineKeyboardMarkup, InlineKeyboardButton)
    text =' افضل مواقع الذكاء الاصطناعي لضغط حجم الصوره اي تقليل مساحتها والحفاظ على جودتها'
    await query.edit_message_text(text, reply_markup = k) 

@bot_pyrogram.on_callback_query (filters.regex('audio_good'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :
    k = audio_good(InlineKeyboardMarkup, InlineKeyboardButton)
    text =' افضل مواقع الذكاء الاصطناعي لتحسين جوده الصوت'
    await query.edit_message_text(text, reply_markup = k) 


@bot_pyrogram.on_callback_query (filters.regex('ai_voice'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :
    k = ai_voice(InlineKeyboardMarkup, InlineKeyboardButton)
    text ='افضل مواقع الذكاء الاصطناعي لتحويل النص الى صوت'
    await query.edit_message_text(text, reply_markup = k) 

@bot_pyrogram.on_callback_query (filters.regex('ai_photo_generator'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :
    k = ai_photo_generator(InlineKeyboardMarkup, InlineKeyboardButton)
    text ='افضل مواقع الذكاء الاصطناعي لتحويل النص الى صوره'
    await query.edit_message_text(text, reply_markup = k) 

@bot_pyrogram.on_callback_query (filters.regex('ai_logo_generator'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :
    k = ai_logo_generator(InlineKeyboardMarkup, InlineKeyboardButton)
    text ='افضل مواقع الذكاء الاصطناعي لتوليد شعار'
    await query.edit_message_text(text, reply_markup = k) 


@bot_pyrogram.on_callback_query (filters.regex('tiktok_installer'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :
    k = tiktok_installer(InlineKeyboardMarkup, InlineKeyboardButton)
    text ='افضل مواقع الذكاء الاصطناعي لازاله العلامه المائيه لفيديوهات التيك توك'
    await query.edit_message_text(text, reply_markup = k) 





@bot_pyrogram.on_callback_query (filters.regex('رجوع'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :
        text = '''افضل مواقع الذكاء الاصطناعي'''

        # # ارسال الرساله الترحيبيه
        # await bot.send_message(user_id, text, reply_markup=replay_markup)

        k = ai_web(InlineKeyboardMarkup, InlineKeyboardButton)

        await query.edit_message_text(text, reply_markup = k)

        

#================================================
#================================================
@bot_pyrogram.on_message(filters.regex('هاشتاغات'))
async def pages_(bot:Client, msg:Message):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    #حفظ id المستخدم فقط اذا ضغط ستارت start 
    if user_id not in data:
        data.append(user_id)
        write(db_path, data)

        # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:

        text = '''لقد اتحنا لك اكثر من 200 هاشتاج من كل صنف تساعدك على صناعه المحتوى'''

        k = hastags_tips(InlineKeyboardMarkup, InlineKeyboardButton)

        await msg.reply_text(text,reply_markup=k,disable_web_page_preview=True)	

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		
	
@bot_pyrogram.on_callback_query (filters.regex('general_hashtags'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :

    k = general_hashtags_tipe(InlineKeyboardMarkup, InlineKeyboardButton)
    text = '''ما المنصه الذي تريد اشهر الهاشتاجات الموجوده بها'''
    await query.edit_message_text(text, reply_markup = k)

@bot_pyrogram.on_callback_query (filters.regex('specific_hashtags'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :

    k = specific_hashtags(InlineKeyboardMarkup, InlineKeyboardButton)
    text = '''ما المحتوى الذي تقوم بنشر عنه اختر الهاشتاجات الخاصه به'''
    await query.edit_message_text(text, reply_markup = k)

@bot_pyrogram.on_callback_query (filters.regex('animals'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :

    a = random.randint(1 , 8)
    if a == 1:
        aa = read_text('hashtags/specific hashtags/animals/animal1 1.txt')
        await query.edit_message_text(aa)
    elif a == 2:
        aa = read_text('hashtags/specific hashtags/animals/animal1 2.txt')
        await query.edit_message_text(aa)
    elif a == 3:
        aa = read_text('hashtags/specific hashtags/animals/animal1 3.txt')
        await query.edit_message_text(aa)
    elif a == 4:
        aa = read_text('hashtags/specific hashtags/animals/animal1 4.txt')
        await query.edit_message_text(aa)
    elif a == 5:
        aa = read_text('hashtags/specific hashtags/animals/animal1 5.txt')
        await query.edit_message_text(aa)
    elif a == 6:
        aa = read_text('hashtags/specific hashtags/animals/animal1 6.txt')
        await query.edit_message_text(aa)
    elif a == 7:
        aa = read_text('hashtags/specific hashtags/animals/animal1 7.txt')
        await query.edit_message_text(aa)
    elif a == 8:
        aa = read_text('hashtags/specific hashtags/animals/animal1 8.txt')
        await query.edit_message_text(aa)
    
@bot_pyrogram.on_callback_query (filters.regex('book'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :
    a = random.randint(1 , 5)
    if a == 1:
        aa = read_text('hashtags/specific hashtags/book/book 1.txt')
        await query.edit_message_text(aa)
    elif a == 2:
        aa = read_text('hashtags/specific hashtags/book/book 2.txt')
        await query.edit_message_text(aa)
    elif a == 3:
        aa = read_text('hashtags/specific hashtags/book/book 3.txt')
        await query.edit_message_text(aa)
    elif a == 4:
        aa = read_text('hashtags/specific hashtags/book/book 4.txt')
        await query.edit_message_text(aa)
    elif a == 5:
        aa = read_text('hashtags/specific hashtags/book/book 5.txt')
        await query.edit_message_text(aa)


@bot_pyrogram.on_callback_query (filters.regex('cars'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :
    a = random.randint(1 , 20)
    if a == 1:
        aa = read_text('hashtags/specific hashtags/cars/car 1.txt')
        await query.edit_message_text(aa)
    elif a == 2:
        aa = read_text('hashtags/specific hashtags/cars/car 2.txt')
        await query.edit_message_text(aa)
    elif a == 3:
        aa = read_text('hashtags/specific hashtags/cars/car 3.txt')
        await query.edit_message_text(aa)
    elif a == 4:
        aa = read_text('hashtags/specific hashtags/cars/car 4.txt')
        await query.edit_message_text(aa)
    elif a == 5:
        aa = read_text('hashtags/specific hashtags/cars/car 5.txt')
        await query.edit_message_text(aa)
    elif a == 6:
        aa = read_text('hashtags/specific hashtags/cars/car 6.txt')
        await query.edit_message_text(aa)
    elif a == 7:
        aa = read_text('hashtags/specific hashtags/cars/car 7.txt')
        await query.edit_message_text(aa)
    elif a == 8:
        aa = read_text('hashtags/specific hashtags/cars/car 8.txt')
        await query.edit_message_text(aa)
    elif a == 9:
        aa = read_text('hashtags/specific hashtags/cars/car 9.txt')
        await query.edit_message_text(aa)
    elif a == 10:
        aa = read_text('hashtags/specific hashtags/cars/car 10.txt')
        await query.edit_message_text(aa)
    elif a == 11:
        aa = read_text('hashtags/specific hashtags/cars/car 11.txt')
        await query.edit_message_text(aa)
    elif a == 12:
        aa = read_text('hashtags/specific hashtags/cars/car 12.txt')
        await query.edit_message_text(aa)
    elif a == 13:
        aa = read_text('hashtags/specific hashtags/cars/car 13.txt')
        await query.edit_message_text(aa)
    elif a == 14:
        aa = read_text('hashtags/specific hashtags/cars/car 14.txt')
        await query.edit_message_text(aa)
    elif a == 15:
        aa = read_text('hashtags/specific hashtags/cars/car 15.txt')
        await query.edit_message_text(aa)
    elif a == 16:
        aa = read_text('hashtags/specific hashtags/cars/car 16.txt')
        await query.edit_message_text(aa)
    elif a == 17:
        aa = read_text('hashtags/specific hashtags/cars/car 17.txt')
        await query.edit_message_text(aa)
    elif a == 18:
        aa = read_text('hashtags/specific hashtags/cars/car 18.txt')
        await query.edit_message_text(aa)
    elif a == 19:
        aa = read_text('hashtags/specific hashtags/cars/car 19.txt')
        await query.edit_message_text(aa)
    elif a == 20:
        aa = read_text('hashtags/specific hashtags/cars/car 20.txt')
        await query.edit_message_text(aa)
 
@bot_pyrogram.on_callback_query (filters.regex('food'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :
    a = random.randint(1 , 5)
    if a == 1:
        aa = read_text('hashtags/specific hashtags/food/Food 1.txt')
        await query.edit_message_text(aa)
    elif a == 2:
        aa = read_text('hashtags/specific hashtags/food/Food 2.txt')
        await query.edit_message_text(aa)
    elif a == 3:
        aa = read_text('hashtags/specific hashtags/food/Food 3.txt')
        await query.edit_message_text(aa)
    elif a == 4:
        aa = read_text('hashtags/specific hashtags/food/Food 4.txt')
        await query.edit_message_text(aa)
    elif a == 5:
        aa = read_text('hashtags/specific hashtags/food/Food 5.txt')
        await query.edit_message_text(aa)


@bot_pyrogram.on_callback_query (filters.regex('space'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :
    a = random.randint(1 , 5)
    if a == 1:
        aa = read_text('hashtags/specific hashtags/Space/Space 1.txt')
        await query.edit_message_text(aa)
    elif a == 2:
        aa = read_text('hashtags/specific hashtags/Space/Space 2.txt')
        await query.edit_message_text(aa)
    elif a == 3:
        aa = read_text('hashtags/specific hashtags/Space/Space 3.txt')
        await query.edit_message_text(aa)
    elif a == 4:
        aa = read_text('hashtags/specific hashtags/Space/Space 4.txt')
        await query.edit_message_text(aa)
    elif a == 5:
        aa = read_text('hashtags/specific hashtags/Space/Space 5.txt')
        await query.edit_message_text(aa)


@bot_pyrogram.on_callback_query (filters.regex('sport'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :

    a = random.randint(1 , 5)
    if a == 1:
        aa = read_text('hashtags/specific hashtags/sport/sport 1.txt')
        await query.edit_message_text(aa)
    elif a == 2:
        aa = read_text('hashtags/specific hashtags/sport/sport 2.txt')
        await query.edit_message_text(aa)
    elif a == 3:
        aa = read_text('hashtags/specific hashtags/sport/sport 3.txt')
        await query.edit_message_text(aa)
    elif a == 4:
        aa = read_text('hashtags/specific hashtags/sport/sport 4.txt')
        await query.edit_message_text(aa)
    elif a == 5:
        aa = read_text('hashtags/specific hashtags/sport/sport 5.txt')
        await query.edit_message_text(aa)


@bot_pyrogram.on_callback_query (filters.regex('nature'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :
    a = random.randint(1 , 20)
    if a == 1:
        aa = read_text('hashtags/specific hashtags/nature/nature 1.txt')
        await query.edit_message_text(aa)
    elif a == 2:
        aa = read_text('hashtags/specific hashtags/nature/nature 2.txt')
        await query.edit_message_text(aa)
    elif a == 3:
        aa = read_text('hashtags/specific hashtags/nature/nature 3.txt')
        await query.edit_message_text(aa)
    elif a == 4:
        aa = read_text('hashtags/specific hashtags/nature/nature 4.txt')
        await query.edit_message_text(aa)
    elif a == 5:
        aa = read_text('hashtags/specific hashtags/nature/nature 5.txt')
        await query.edit_message_text(aa)
    elif a == 6:
        aa = read_text('hashtags/specific hashtags/nature/nature 6.txt')
        await query.edit_message_text(aa)
    elif a == 7:
        aa = read_text('hashtags/specific hashtags/nature/nature 7.txt')
        await query.edit_message_text(aa)
    elif a == 8:
        aa = read_text('hashtags/specific hashtags/nature/nature 8.txt')
        await query.edit_message_text(aa)
    elif a == 9:
        aa = read_text('hashtags/specific hashtags/nature/nature 9.txt')
        await query.edit_message_text(aa)
    elif a == 10:
        aa = read_text('hashtags/specific hashtags/nature/nature 10.txt')
        await query.edit_message_text(aa)

@bot_pyrogram.on_callback_query (filters.regex('instagram_hashtags'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :
    a = read_text('hashtags/general hashtags/instgram.txt')
    await query.edit_message_text(a)

@bot_pyrogram.on_callback_query (filters.regex('tiktok_hashtags'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :
    a = read_text('hashtags/general hashtags/tik tok.txt')
    await query.edit_message_text(a)


@bot_pyrogram.on_callback_query (filters.regex('back0'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :
        text = '''لقد اتحنا لك اكثر من 200 هاشتاج من كل صنف تساعدك على صناعه المحتوى'''

        k = hastags_tips(InlineKeyboardMarkup, InlineKeyboardButton)

        await query.edit_message_text(text, reply_markup = k)
#================================================
#================================================
      
@bot_pyrogram.on_callback_query (filters.regex('buffer'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :

    await buffer(query, InlineKeyboardMarkup, InlineKeyboardButton)

@bot_pyrogram.on_callback_query (filters.regex('metricool'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :

    await metricool(query, InlineKeyboardMarkup, InlineKeyboardButton)

@bot_pyrogram.on_callback_query (filters.regex('back_web'))
async def handle_button_click ( bot:Client, query:CallbackQuery ) :
        text = '''افضل المواقع لجدوله المنشورات '''

        # # ارسال الرساله الترحيبيه
        # await bot.send_message(user_id, text, reply_markup=replay_markup)

        k = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(f"buffer", callback_data='buffer')
                    ],
                    [
                        InlineKeyboardButton(f"metricool", callback_data='metricool')
                    ]
                ]
            )
        await query.edit_message_text(text, reply_markup = k)

#================================================
#================================================
@bot_pyrogram.on_message(filters.regex('افضل الهوكس'))
async def pages_(bot:Client, msg):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id


    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        a = '''
كيف نحل "نوع المشكله" 3 خطوات

عندك نوع "المشكله الذي يواجهها المستخدم" خليني اقول لك كيف تحلها

كيف انتقلت من "نوع المشكله الذي كنت اعاني منها"   "للنتيجه الذي وصلتها  عندما اتبعت هذا الاسلوب"


ليش "اسم المنتج او الخدمه الذي تقوم بتقديمها"

ثلاث شغلات بيتميز فيها "اسم منتجك او الخدمه يلي بتقدمه"

شو صار بعميل عندي بعد ما استخدم "الخدمه او المنتج اللي انت بتقدمه"

رح قول لك كيف ب "اسم المنتج او الخدمه" حليت المشكله هي "نوع المشكله

عندي شي رح يغير حياتك

هذا السر لا تقولو لحدا

ثلاث شغلات تمنيت لو بعرفهم من زمان

معلومه متاكد ما كنت بتعرفها من قبل

غلط بيوقع فيه اغلب الاشخاص

افضل ثلاث طرق

اسوء ثلاث طرق

شي بتعتبره فعال بس هو عكس هذا الشيء تماما


اذا بدك توصل "الهدف معين" بنهايه "المده معينه"

اذا بتشوف هذا الشيء قبل "تاريخ معين" رح توصل "لهدف معين"

انت ما رح يكون عندك "شيء معين" اذا ما شفت هذا الفيديو

انت ما رح تعرف توصل "لهدف معين" من دون ما تشوف هذا الفيديو

اشياء "صنف معينه من البشر" ما بدها انك تعرفه



ملاحظه مهمه هذه الهوكس الذي تم اضافتها هي اكثر هوكس شائعه ومتداوله بمنصات التواصل الاجتماعي واذا تريد ان يكون لديك هوكس مخصصه لنوع المحتوى الذي تقوم بنشره فهذه بعض النقاط التي يمكنك ان تلتزم بها

يمكنك جذب المشاهدات عن طريق المشاعر اي ان يكون الهوك الخاص بك يحوي قيمه معينه من المشاعر التي يمكن ان تجذب المشاهد

ان ينتظر ويترقب المشاهد رده فعل فيمكن ان يكون الهوك الخاص بك نتيجه لرده فعل ما

ان يكون الهوك يحوي على نسبه معينه من الاستفزاز وليس الاستفزاز بطريقه سلبيه اي بطريقه ايجابيه تدفع المشاهد ليكمل الفيديو

ان تجعل المشاهد يعلم ما هي القيمه التي سيتلقاها مقابل مشاهدته للفيديو الخاص بك

تنويه مهم هذه الهوكس ليست هي السبب الرئيسي والاول لتجعلك مشهور وتجلب لك مشاهدات كبيره فيوجد عده نقاط يرتكز عليها هذا الشيء من بين هذه النقاط نوع المحتوى الذي تقدمه 
 والجمهور المستهدف الهوكس وسيله لجذب المشاهد الذي يهتم بنوع المحتوى الذي انت تقدمه
'''
        await bot.send_message(user_id, a)

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		


# ==================================
#الصفحات

@bot_pyrogram.on_message(filters.regex("YOUTUBE"))
async def pages_(bot:Client, msg):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id


    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        # ارسال الرساله الترحيبيه
        link = 'https://www.youtube.com/channel/UCFtDm5Bdq2KZdWCkmHPiBYw'
        app_name = 'YOUTUBE'
        await link_buttom_for_accounts(msg, link, app_name)

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		

@bot_pyrogram.on_message(filters.regex("FACEBOOK"))
async def pages_(bot:Client, msg):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id


    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        # ارسال الرساله الترحيبيه
        link = 'https://www.facebook.com/profile.php?id=61556736453822'
        app_name = 'FACEBOOK'
        await link_buttom_for_accounts(msg, link, app_name)

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		

@bot_pyrogram.on_message(filters.regex("INSTAGRAM"))
async def pages_(bot:Client, msg):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id


    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        # ارسال الرساله الترحيبيه
        link = 'https://www.instagram.com/_a_randoms_/'
        app_name = 'INSTAGRAM'
        await link_buttom_for_accounts(msg, link, app_name)

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		

@bot_pyrogram.on_message(filters.regex("TIK TOK"))
async def pages_(bot:Client, msg):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id


    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        # ارسال الرساله الترحيبيه
        link = 'https://www.tiktok.com/@_randoms_a_'
        app_name = 'TIK TOK'
        await link_buttom_for_accounts(msg, link, app_name)

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		

@bot_pyrogram.on_message(filters.regex("TELEGRAM"))
async def pages_(bot:Client, msg):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id


    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        # ارسال الرساله الترحيبيه
        link = 't.me/RANDOMS_CH'
        app_name = 'TELEGRAM'
        await link_buttom_for_accounts(msg, link, app_name)

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		

@bot_pyrogram.on_message(filters.regex("BIGO LIVE"))
async def pages_(bot:Client, msg):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id


    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        # ارسال الرساله الترحيبيه
        link = 'https://www.bigo.tv/user/985447292'
        app_name = 'BIGO LIVE'
        await link_buttom_for_accounts(msg, link, app_name)

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		

# ====================================
#للعوده للصفحه الرئيسيه للبوت
@bot_pyrogram.on_message(filters.regex('<<عوده'))
async def pages_(bot:Client, msg):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    #حفظ id المستخدم فقط اذا ضغط ستارت start 
    if user_id not in data:
        data.append(user_id)
        write(db_path, data)

        # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        #الرد بالازرار
        buttoms = buttoms_replay()
        replay_markup = ReplyKeyboardMarkup(buttoms, one_time_keyboard= True, resize_keyboard=True)

        # ارسال الرساله الترحيبيه
        await bot.send_message(user_id, 'عدنا', reply_markup=replay_markup)

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		




if __name__ == '__main__':
    # keep_alive()
    bot_pyrogram.run()

else:
    print('the bot is not work :(')
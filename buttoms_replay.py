
def buttoms_replay():

    replay_message_buttoms = [
        [
            ('صفحاتنا'),
            ('بوتاتنا')
        ],
        [
            ('هاشتاغات')
        ],
        [
            ('مواقع ذكاء اصطناعي')
        ],
        [
            ('مواقع لجدوله المنشورات')
        ],
        [
            ('افضل الهوكس')
        ],
        [
            ('لاي اقتراحات')
        ],
        [
            ('حول البوت')
        ]
    ]

    return replay_message_buttoms


def pages():
    
    replay_message_buttoms = [
        [
            ('YOUTUBE')
        ], 
        [
            ('FACEBOOK')
        ],
        [
            ('INSTAGRAM')
        ],
        [
            ('TIK TOK')
        ], 
        [
            ('TELEGRAM')
        ],
        [
            ('BIGO LIVE')
        ], 
        [
            ('<<عوده')
        ]
    ]

    return replay_message_buttoms


def ai_web(InlineKeyboardMarkup, InlineKeyboardButton):
    k = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"ازالة خلفيه الصور", callback_data='remove_bg')
                ],
                [
                    InlineKeyboardButton(f"رفع جوده الصورة", callback_data='photo_up_scaler')
                ],
                [
                    InlineKeyboardButton("ضغط حجم الصورة", callback_data='photo_Compression')
                ],
                [
                    InlineKeyboardButton(f"تحسين جوده الصوت", callback_data='audio_good')
                ],
                [
                    InlineKeyboardButton("تحويل النص لصوت", callback_data='ai_voice')
                ],
                [
                    InlineKeyboardButton("توليد صور من الكتابة", callback_data='ai_photo_generator')
                ],
                [
                    InlineKeyboardButton("توليد شعار بالذكاء الاصطناعي", callback_data='ai_logo_generator')
                ],
                [
                    InlineKeyboardButton("تحميل فيديوهات tiktok بدون علامة مائية", callback_data='tiktok_installer')
                ]
            ]
        )
    return k


def hastags_tips(InlineKeyboardMarkup, InlineKeyboardButton):
    k = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f'هاشتاغات عامة', callback_data='general_hashtags')
                ],
                [
                    InlineKeyboardButton(f'هاشتاغات مخصصة', callback_data='specific_hashtags')
                ]
            ]
        )
    return k


def general_hashtags_tipe(InlineKeyboardMarkup, InlineKeyboardButton):
    k = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f'instagram hashtags', callback_data='instagram_hashtags')
                ],
                [
                    InlineKeyboardButton('tiktok hashtags', callback_data='tiktok_hashtags')
                ],
                [
                    InlineKeyboardButton('عودة', callback_data='back0')
                ]
            ]
        )
    return k

def specific_hashtags(InlineKeyboardMarkup, InlineKeyboardButton):
    k = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f'animals', callback_data='animals')
                ],
                [
                    InlineKeyboardButton('book', callback_data='book')
                ],                
                [
                    InlineKeyboardButton(f'cars', callback_data='cars')
                ],
                [
                    InlineKeyboardButton('food', callback_data='food')
                ],
                [
                    InlineKeyboardButton('nature', callback_data='nature')
                ],                
                [
                    InlineKeyboardButton('space', callback_data='space')
                ],
                [
                    InlineKeyboardButton('sport', callback_data='sport')
                ],
                [
                    InlineKeyboardButton('عودة', callback_data='back0')
                ]
            ]
        )
    return k


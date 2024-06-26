

def buffer(query, InlineKeyboardMarkup, InlineKeyboardButton):
    text = '''
خطة بوفر المجانية توفر مجموعة محدودة من الميزات لمساعدتك في جدولة المنشورات على وسائل التواصل الاجتماعي. إليك ملخص للخطة المجانية ومدة صلاحيتها:

عدد الحسابات الاجتماعية: يمكنك ربط ما يصل إلى 3 حسابات اجتماعية على منصات مثل تويتر وفيسبوك وإنستجرام وLinkedIn وPinterest في الخطة المجانية.

جدولة المنشورات: يمكنك جدولة حتى 10 منشورات في كل حساب اجتماعي.

التوقيت المحدود: يمكنك تحديد وقت محدد لنشر المنشورات، ولكن هناك توقيت محدود للمنشورات في اليوم الواحد.

تحليلات الأداء: يتم توفير بعض التحليلات الأساسية لأداء المنشورات، مثل عدد المشاهدات والتفاعلات.

تجدر الإشارة إلى أن الخطة المجانية لبوفر توفر مستوى أساسيًا من الوظائف، ولكن قد يكون هناك قيود على عدد المنشورات والتوقيت. يمكنك الاستفادة من هذه الخطة للتعرف على واجهة بوفر واستكشاف ميزاتها قبل الاشتراك في الخطط المدفوعة.

بالنسبة لمدة صلاحية الخطة المجانية، فإنها تستمر إلى الأبد. يمكنك استخدام الخطة المجانية مدى الحياة دون الحاجة إلى الترقية إلى الخطط المدفوعة. ومع ذلك، قد يكون هناك تحديثات وتغييرات في السياسة والميزات التي قد تؤثر على خطة الاستخدام المجانية في المستقبل.    
'''

    k = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"buffer",url=f'http://www.buffer.com/')
                ],
                [
                    InlineKeyboardButton(f'<<رجوع', callback_data='back_web')
                ]
            ]
            )
    a = query.edit_message_text(text, reply_markup = k)
    return a

def metricool(query, InlineKeyboardMarkup, InlineKeyboardButton):
    text = '''

خدمة Metricool هي أداة لجدولة المنشورات وإدارة وسائل التواصل الاجتماعي. توفر خطة مجانية تتيح للمستخدمين استخدام بعض الميزات الأساسية. إليك نظرة عامة على خدمة Metricool وخطتها المجانية:

جدولة المنشورات: يمكنك جدولة المنشورات على منصات التواصل الاجتماعي الشهيرة مثل تويتر، إنستجرام، فيسبوك، ولينكد إن. يمكنك تحديد التوقيت الذي ترغب في نشر المنشورات.

تقويم التحليلات: توفر Metricool بيانات تحليلية مفصلة حول أداء منشوراتك وحساباتك على وسائل التواصل الاجتماعي. يمكنك مراقبة مقاييس الوصول والانخفاضات والتفاعلات ومعدلات الارتباط.

مراقبة المنافسين: توفر Metricool أداة لمراقبة أنشطة المنافسين على وسائل التواصل الاجتماعي، مما يساعدك على فهم استراتيجياتهم ومقارنتها مع أداءك الخاص.

تقارير محدودة: يمكنك إنشاء تقارير بسيطة حول أداء حساباتك على وسائل التواصل الاجتماعي وتصديرها في الخطة المجانية.

تُرجم Metricool إلى العديد من اللغات، بما في ذلك الإنجليزية، وتعتبر خدمة شهيرة وموثوقة في مجال إدارة وسائل التواصل الاجتماعي. 
يتيح لك جدوله 50 منشور في الشهر الواحد و يتجدد كل شهر
خدمة Metricool توفر خطة مجانية تسمح للمستخدمين بالاستفادة من الميزات الأساسية مدى الحياة دون الحاجة إلى الاشتراك في الخطط المدفوعة. يمكنك استخدام الخدمة المجانية بدون تاريخ انتهاء صلاحيتها.
يمكنك زيارة موقع Metricool والتسجيل للحصول على حساب مجاني واستكشاف المزيد من الميزات التي تقدمها الخدمة.
'''
    
    k = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"metricool",url=f"https://metricool.com/")
                ],
                [
                    InlineKeyboardButton(f'<<رجوع', callback_data='back_web')
                ]
            ]
            ) 
    a = query.edit_message_text(text, reply_markup = k)
    return a
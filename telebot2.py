import telebot
from telebot import types
import random

bot = telebot.TeleBot('1895188331:AAE7dOhDVdIxqPwCmCL8Bf4-Oh9QYQusszM')
questions = [
    #stage 1
    [

        [
            'Благодаря какому интернет-правилу виртуальный ассистент от компании Samsung стала популярной?',
            ['правило 34', 'правило 69' , 'правило 34.5' , 'правило левой руки']
        ],
        [
            'Моршу. В какой игре появился данный персонаж?',
            ['Link: The Faces of Evil', 'The Elders Scrolls: Arena', 'это рукотворный мем, не привязанный к игре', 'The legend of Zelda']
        ],
        [
            'Что продаёт Моршу в своей лавке?',
            ['масло для лампы, верёвку и бомбы', 'верёвку и мыло', 'оружие и броню', 'зелья лечения']
        ],
        [
            'Амогус.Персонаж какой игры породил данный мем?',
            ['Аmong us', 'Mafia II', 'Fall Guys', 'GTA San Andreas']
        ],
    ],
    #stage 2
    [
        [
            'Какое значение носит мем Амогус?',
            ['постыроничный мем без смысла', 'глубокий смысл ничтожности нашего бытия', 'самоирония разработчиков', 'символ мультяшных игр в мировой культуре']
        ],
        [
            'Ура, я умнее, чем компьютеp! Персонаж какой игры произносит данную фразу?',
            ['Малыш 3', 'Fallout tactics', 'Братья Пилоты: Обратная сторона земли', 'Transformers: Rise of the Dark Spark']
        ],
        [
            'Сержант Дорнан. Сколько лет должен будет служить герой в армии Анклава в случае утери силовой брони модель 2?',
            ['510', '20', '30', '100']
        ],
        [
            'Какого пола Сержант Дорнан?',
            ['женщина', 'мужчина', 'агендер', 'боевой вертолет']
        ],
    ],
    #stage 3
    [
        [
            'Какой породы собаки из мема про накаченного и худого пса?',
            ['сиба-ину', 'тибетские мастиффы', 'акита-ину', 'немецкие овчарки']
        ],
        [
            'Как зовут собак из мема про накаченного и худого пса?',
            ['Доге и Чимс', 'Ичико и Ибиро', 'Чип и Дейл', 'Забуза и Хаку'],
        ],
	[
            'К какому виду принадлежит Шлёпа?',
            ['Каракал', 'Кот домашний', 'Рысь', 'Тигр'],
        ],
	[
            'Рецепт какого блюда рассказывал Шлёпа?',
            ['пельмени', 'вареники', 'драники', 'паштет из хлебного варенья'],
        ]
    ],
    #stage 4
    [
        [
            'Из какой серии игр происходит фраза “Чики-брики и в дамки!”?',
            ['S.T.A.L.K.E.R', 'Fallout', 'D.o.t.A', 'Metro 2033']
        ],
        [
            'Персонаж какой фракции произносит фразу “Чики-брики и в дамки!”?',
            ['Чистое Небо', 'Долг', 'Бандиты', 'Свобода']
        ],
	[
            'Чью маску носят анонимусы?',
            ['гая фокса', 'амогуса', 'маска была придумана специально для анонимусов', 'джимми нейтрона']
        ]
    ],
]

sessions = {}

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global sessions;
    global questions;
    keyboard = types.InlineKeyboardMarkup()
    if message.text == '/start':
        stage = 1
        sessions[message.from_user.id] = stage
        print("start: user_id=" + str(message.from_user.id))
        q_list = questions[stage - 1]
        q_num = random.randint(0, len(q_list) - 1)
        item = q_list[q_num]
        question_text = item[0]
        answer_list = item[1];

        bot.send_message(message.from_user.id, ("Привет, вот первый вопрос: " + question_text))
        temp = [0,1,2,3]
        random.shuffle(temp)
        for i in temp:
            if i == 0:
                answer_id = stage
            else:
                answer_id = str(stage) + '_' + str(q_num + 1) + '_' + str(i + 1)
                
            key = types.InlineKeyboardButton(text=answer_list[i], callback_data = answer_id)
            keyboard.add(key)
        bot.send_message(message.from_user.id, 'выбери верный ответ:', reply_markup = keyboard)
        ####
    else:
        bot.send_message(message.from_user.id, 'Напиши /start чтобы начать викторину')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global sessions;
    global questions;
    
    keyboard = types.InlineKeyboardMarkup()
    
    print(call.data)
    print(call.message.chat.id)
    if call.message.chat.id in sessions and sessions[call.message.chat.id] != False:
        stage = sessions[call.message.chat.id]
        
        if stage == 1 and call.data == '1':
            stage = 2
            sessions[call.message.chat.id] = stage
            ###
            q_list = questions[stage - 1]
            q_num = random.randint(0, len(q_list) - 1)
            item = q_list[q_num]
            question_text = item[0]
            answer_list = item[1];

            bot.send_message(call.message.chat.id, ('Поздравляю, это верный ответ. Вот второй вопрос: ' + question_text))
        
            temp = [0,1,2,3]
            random.shuffle(temp)
            for i in temp:
                if i == 0:
                    answer_id = stage
                else:
                    answer_id = str(stage) + '_' + str(q_num + 1) + '_' + str(i + 1)
                key = types.InlineKeyboardButton(text=answer_list[i], callback_data = answer_id)
                keyboard.add(key)
            bot.send_message(call.message.chat.id, 'выбери верный ответ:', reply_markup = keyboard)
            return
            
        
        if stage == 2 and call.data == '2':
            stage = 3
            sessions[call.message.chat.id] = stage
            q_list = questions[stage - 1]
            q_num = random.randint(0, len(q_list) - 1)
            item = q_list[q_num]
            question_text = item[0]
            answer_list = item[1];

            bot.send_message(call.message.chat.id, ('Поздравляю, это верный ответ. Вот третий вопрос: ' + question_text))
        
            temp = [0,1,2,3]
            random.shuffle(temp)
            for i in temp:
                if i == 0:
                    answer_id = stage
                else:
                    answer_id = str(stage) + '_' + str(q_num + 1) + '_' + str(i + 1)
                key = types.InlineKeyboardButton(text=answer_list[i], callback_data = answer_id)
                keyboard.add(key)
            bot.send_message(call.message.chat.id, 'выбери верный ответ:', reply_markup = keyboard)
            return
           
        if stage == 3 and call.data == '3':
            stage = 4
            sessions[call.message.chat.id] = stage
            q_list = questions[stage - 1]
            q_num = random.randint(0, len(q_list) - 1)
            item = q_list[q_num]
            question_text = item[0]
            answer_list = item[1];

            bot.send_message(call.message.chat.id, ('Поздравляю, это верный ответ. Вот четвертый вопрос: ' + question_text))
        
            temp = [0,1,2,3]
            random.shuffle(temp)
            for i in temp:
                if i == 0:
                    answer_id = stage
                else:
                    answer_id = str(stage) + '_' + str(q_num + 1) + '_' + str(i + 1)
                key = types.InlineKeyboardButton(text=answer_list[i], callback_data = answer_id)
                keyboard.add(key)
            bot.send_message(call.message.chat.id, 'выбери верный ответ:', reply_markup = keyboard)
            return


        if stage == 4 and call.data == '4':
            bot.send_message(call.message.chat.id, 'Поздравляю, это верный ответ. Ты выиграл!!! ')
            sessions[call.message.chat.id] = False
            return

        if stage == 4:
            bot.send_message(call.message.chat.id, 'Ты проиграл на последнем вопросе( введи /start чтобы начать заново')
        else:
            bot.send_message(call.message.chat.id, 'Это неверный ответ, напиши /start чтобы начать заново')

        sessions[call.message.chat.id] = False
        

bot.polling(none_stop=True, interval=0)

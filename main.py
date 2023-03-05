from googletrans import Translator

translator = Translator()
matn = "Salom Dunyo"
tarjima = translator.translate(matn, dest='en')

print(tarjima.text)


from telegram.ext import Updater, CallbackContext, ConversationHandler, CommandHandler, MessageHandler, Filters
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from googletrans import Translator

updater = Updater(token="", use_context=True)


TEXT, LANGUAGE = range(2)


def start(update: Update, context: CallbackContext):
    ism = update.effective_user.first_name
    familiya = update.effective_user.last_name
    update.message.reply_text(f"Salom {ism} {familiya} botga xush kelibsiz!! Tarjima qilish uchun textni yuboring")
    return TEXT


def text_to_translate(update: Update, context: CallbackContext):
    text = update.message.text
    languages = ['uz', 'en', 'ru']
    buttons = [[KeyboardButton(language) for language in languages]]
    reply_buttons = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)  # resize_keyboard --> komp yoki telefin uchun qulaylik yaratib beradi
    update.message.reply_text("Kerakli tilni tanlang!", reply_markup=reply_buttons)
    context.user_data['text'] = text
    return LANGUAGE

def translator(update: Update, context: CallbackContext):
    language = update.message.text
    text = context.user_data['text']
    tarjimon = Translator()
    tarjima = tarjimon.translate(text, dest=language).text




    update.message.reply_text(f"Tarjima qilingan text: {tarjima}\nYana text tarjima uchun /start buyrug'idan foydalaning!")

    # return start(update, context)  # davom etoradi qayta yuborish togridan togri

    return ConversationHandler.END   # tugatadi conversationni


#ob havoni eski kodini oling searchda yozilganini

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={TEXT: [MessageHandler(Filters.text, text_to_translate)],
            LANGUAGE: [MessageHandler(Filters.regex("^(uz|en|ru)$"), translator)]},   # "ragex' --> foydalanuvchi har qanaqa malumot berolmaydi ragex orqali bolgan malumotlarnigina chiqaraoladi
    fallbacks=[],

)
dispatcher = updater.dispatcher
dispatcher.add_handler(conv_handler)   # aynan "START" funksiyasini ishga tushirish uchun "Dispatcher.add" funksiyasi kerak boladi
updater.start_polling()
updater.idle()



#Show list
#Choose category key
#Choose item value
#Choose amount

#
# list = []
#
# dict = {'fruits':['apple', 'banana', 'apricot', 'grape', 'pomegranate'],
#         'vegatables':['tomato', 'potato', 'cucumber', 'carrot', 'radish'],
#         'drinks':['cola', 'fanta', 'pepsi', 'apple juice', 'lemon tea']}
#
# print(dict)
#
# for i in dict.keys():
#     print(i)
#
# for i in dict.values():
#     print(i)
#
# for i in dict.items():
#     print(i)
#
#
# my_dict = {'fruits': ["apple", "grapes", "pineaple"], "f_price": [2, 5, 1.5]}
# korzinka = []
# amounts = []
# while True:
#     menu = input("THIS IS MENU: ")
#     if menu == "1":
#         print(my_dict["fruits"])
#     elif menu == "2":
#         while True:
#
#             category = input("choose category: ")
#             if category != "q":
#                 print(my_dict[category])
#                 item = input("CHOOSE ITEM: ")
#                 korzinka.append(item)
#                 amount = input("HOW MUCH U WANT: ")
#                 amounts.append(amount)
#             elif category == "q":
#                 break
#
#     elif menu == "3":
#         print("YOUR KORZINKA: ")
#
#         dict2 = {"Your ITEMS" : korzinka, "AMOUNT" : amounts}



# page:
# 1. Sign in
# 2. Register
# 3. Quit

# page: Sign in
# input - username:
# input - password

# s. -->


# s = 'Men CIU da 2 kurs talabasiman, 2003 yilda tugilganman.'
#
#
# s = s.split()
# # print(s)
# for i in s:
#     if i.isdigit():
#         print(i)
#
#
# #malumotlar tuzilmasi va algoritmlar
#
# i = 0
# a = [1, 2, 3, 4, 5, 8, 7, 9, 0]
# for k in range(len(gls)-1):
#
#
# # class -->


# import random
# list = [5, 7, 12, 25, 37, 56, 79, 95]
# print(list)
#
# # MAX
# max = list[0]
# for x in list:
#     if x > max:
#         max = x
# print(max)
#
# # MIN
# min = list[0]
# for x in list:
#     if x < min:
#         min = x
# print(min)

# ODD NUMBERS


# class Stack:
#     def __init__(self):
#         self.list=[]
#     def push(self,k):
#         self.list.insert(0,k)
#     def pop(self):
#         self.list.pop(0)
#     def top(self):
#         return self.list[0]
#     def size(self):
#         return len(self.list)
#     def isEmpty(self):
#         if(size(self)==0):
#             return True
#         else: return False
#     def pr(self):
#         print(self.list)
# st1=Stack()
# n=int(input('n='))
# for i in range(n):
#     st1.push(input('son='))
# print('boshlangich holat:')
# st1.pr()
# k=input('urtaga kiritiladigan son=')
# st2=Stack()
# for i in range(n//2):
#     st2.push(st1.top())
#     st1.pop()
# st1.push(k)
# for i in range(n//2):
#     st1.push(st2.top())
#     st2.pop()
# print('keyingi holat:')
# st1.pr()


# n=7  ---> CONSOLEDAGI NATIJA
# son=1
# son=2
# son=3
# son=4
# son=5
# son=6
# son=7
# boshlangich holat:
# ['7', '6', '5', '4', '3', '2', '1']
# urtaga kiritiladigan son=2003
# keyingi holat:
# ['7', '6', '5', '2003', '4', '3', '2', '1']








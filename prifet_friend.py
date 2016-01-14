# -*- coding: utf-8 -*-

import vk
import random
import time

acc_tok = 'your access token'
session = vk.Session(access_token=acc_tok)
api = vk.API(session)

mode = raw_input( \
	'''What mode do you want to use:\n
	1.fence
	2.translation to english
	3.leet
	''')

if mode == "2":
	from yandex_translate import YandexTranslate
	translate = YandexTranslate('your access token')

if mode == '3':
	idiots_dict = \
	{ 
		u'А':'4', u'а':'4', u'Б':'6', u'б':'6', u'в':'8', u'В':'8', u'г':'Г', 
		u'д':'g', u'Е':'3', u'е':'3', u'Ж':'>|<', u'ж':'>|<', u'З':'3', u'з':'3', 
		u'и':'N', u'И':'N', u'К':'k', u'к':'k', u'Л':'/\\', u'л':'/\\', u'м':'М', 
		u'н':'Н', u'о':'0', u'О':'0', u'п':'П', u'р':'Р', u'с':'S', u'С':'S', 
		u'Т':'7', u'т':'7', u'У':'Y', u'у':'Y', u'ц':'С', u'Ц':'C', u'Ч':'4', 
		u'ч':'4', u'Ш':'LLI', u'ш':'LLI', u'Ы':'bl', u'ы':'bl', u'ь':'b', u'Ь':'b',
		u'я':'9l', u'Я':'9l'
	}

friend_id = raw_input('Enter your friend id: ')
number_of_last_messages = 15
history_list = api.messages.getHistory(user_id=friend_id, count=str(number_of_last_messages))
current_mid = history_list[number_of_last_messages]['mid']

while True:
	try:
		list_of_messages = api.messages.getHistory(user_id=friend_id, count='15', rev='0')
		list_of_messages = list_of_messages[1::]
		list_of_messages = [x for x in list_of_messages if x['mid'] > current_mid]
		for i in range(0, len(list_of_messages)):
			print('---' + list_of_messages[len(list_of_messages) - i - 1]['body'])
		if (len(list_of_messages)):
			current_mid = list_of_messages[0]['mid']
		time.sleep(1)
	except KeyboardInterrupt:
		message = raw_input(':').decode('utf-8')
		mEsSaGe = ''
		if mode == '2':
			mEsSaGe = translate.translate(message, 'ru-en')['text']
		elif mode == '1':
			for i in range(len(message)):
				if i % 2 != 0:
					mEsSaGe += message[i].upper()
				else: mEsSaGe += message[i]
		elif mode == '3':
			for letter in message:
				if letter in idiots_dict:
					mEsSaGe += idiots_dict[letter]
				else: mEsSaGe += letter.encode('utf-8')
		
		sent_message_int = api.messages.send(user_id=friend_id, message=mEsSaGe)
		sent_message_list = [sent_message_int]
		current_message_id_list = api.messages.getById(message_ids=sent_message_list)	
		current_mid = current_message_id_list[1]['mid']
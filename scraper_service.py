from deep_translator.exceptions import  RequestError
from deep_translator import GoogleTranslator
from langdetect import detect
import datetime
import re
from sessions import client_max
async def retreive_message_keyword(client,channel, keywords, hours):
    time=datetime.datetime.now() - datetime.timedelta(hours=hours)
    results = await client.get_messages(channel, limit=None, offset_date= time, reverse=True)
    filtered=[]
    translated_keywords=[]

    #translating keywords
    for k in keywords:
        if not bool(re.search('[а-яА-Я]', k)):
            translated_keyword_ru=GoogleTranslator(source='en', target='ru').translate(k[1:])
            translated_keyword_ukr=GoogleTranslator(source='en', target='uk').translate(k[1:])
            if translated_keyword_ukr == translated_keyword_ru:
                translated_keywords.append(k)
                translated_keywords.append(f'${translated_keyword_ukr}')
            else:
                translated_keywords.append(k)
                translated_keywords.append(f'${translated_keyword_ukr}')
                translated_keywords.append(f'${translated_keyword_ru}')
        else:
            translated_keywords.append(k)

    # checking for presence of keywords in message
    for i in results:
        for keyword in translated_keywords:
            if keyword[1:] in i.message:
                lang = detect(i.message)
                if lang != "en":
                    translated_message = GoogleTranslator(source='auto', target='en').translate(i.message)
                    filtered.append([i,translated_message])
                else:
                    filtered.append([i])
    return filtered


async def retreive_message(client,channel, hours):
    await client_max.connect()
    if not await client.is_user_authorized():
        await client.send_code_request("+17573582912")
        await client.sign_in("+17573582912", input('Enter the code: '))

    time = datetime.datetime.now() - datetime.timedelta(hours=hours)
    retrieved_messages = await client.get_messages(channel, limit=None, offset_date=time, reverse=True)
    filtered = []
    for m in retrieved_messages:
        if m.message != "" and m.message != None:
            lang = detect(m.message)



            #translating message
            if lang != "en":
                try:
                    translated_message = GoogleTranslator(source='auto', target='en').translate(m.message)
                    filtered.append([m, translated_message])
                except RequestError as request_e:
                    pass
            else:
                filtered.append([m])
    return print(filtered)
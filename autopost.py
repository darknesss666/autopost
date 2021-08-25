import vk
import time
import traceback
from ast import literal_eval

TOKEN = input('🔐Введи ниже токен:\n')
session = vk.Session(access_token = TOKEN)
vk_api = vk.API(session, v='5.135')

GROUPS = literal_eval(input('Введи ниже айди групп с минусом или айди человека, куда будет выложен пост, не забудь добавить квадратные скобки:\n'))
SMS = input(f'Введи ниже текст сообщения, которое будет опубликовано:\n')
try:
    for a in GROUPS:
        vk_api.wall.post(owner_id = a, from_group = 0, message = SMS)
    time.sleep(5)
except vk_api.exceptions.Captcha as captcha:
    captcha.sid
    print(f'Появилась капча - {captcha.get_url()}')
    captcha_key = input('Реши капчу: ')
    captcha.try_again(captcha_key) 
except vk_api.exceptions.VkApiError:
    traceback.print_exc()
print('''\033[1;32mРассылка закончена✅.
\033[0m\033[33mСкрипт написал Кирилл Элатов.
ВКонтакте создателя скрипта: https://vk.com/i____hate____my____life''')
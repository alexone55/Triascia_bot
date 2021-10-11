import os
import telebot
from dotenv import load_dotenv


load_dotenv("./resources/.env")
OUR_GROUP = os.getenv('OUR_GROUP')
BOT_TOKEN = os.getenv('BOT_TOKEN')
RULE_TEXT = f'*Що там по правилам?*' \
                 f'\n' \
                 f'\n1. Використовувати стікери у боті _не_ рекомендується, ' \
                 f'користуйтеся передбаченими опціями. ' \
                 f'Приклад: /rules, /questions, /guarantees.' \
                 f'\n' \
                 f'\n2. Чітко формулюйте свій запит _без агресії_ одним повідомленням.' \
                 f'\n' \
                 f'\n3. Для отримання послуг з написання курсової/дипломної роботи, _одразу зазначайте у хештегу_, ' \
                 f'якої спрямованості робота #політологія, #туризм, #хімія, #математика тощо.' \
                 f'\n' \
                 f'\n4. Щоб наша робота була плідною, всі _методичні рекомендації_ з ' \
                 f'написання надсилайте doc/docx/pdf файлом.' \
                 f'\n' \
                 f'\n5. Виставляйте _дедлайни_. Якщо вас цікавлять послуги рефератів до ' \
                 f'курсових/дипломних робіт та презентації - скористайтеся хештегом /option.' \
                 f'\n' \
                 f'\n6. _Менторську допомогу_ можна отримати за хештегом /mentors.' \


GUARANTEE_TEXT = f'*Що там по гарантіям?*\n' \
                 f'\nЗі свого боку ми _зобов\'язуємося_ дотримуватися конфіденційності і не розповсюджувати ' \
                 f'інформації щодо нашої допомоги вам. _Все анонімно_. Робимо все згідно дедлайнам, ' \
                 f'при їх недотриманні – робимо знижку. На кожному етапі роботи ми надаємо звіт, ' \
                 f'бо головне для нас це прозорість.\n' \
                 f'\nЩоб скористатися послугою з написання наукової роботи, просимо вас вносити _передоплату у 30%_.' \
                 f' На кожному проміжному файлі ми ставимо водяний знак, як гарантія і нашої, і вашої безпеки.\n' \
                 f'\n*З вашого боку ми очікуємо хороших відгуків :)*'

HELLO_TEXT = f'«Трясця, забув про курсову» – проєкт для тих, хто не знає, ' \
             f'навіщо писати наукові роботи, не справляється з ' \
             f'купою вимог або просто не хоче (і це нормально!)'

bot = telebot.TeleBot(BOT_TOKEN)
from core.message_hendlers import supergroup_message_handlers
from core.callback_handlers import guarantee_hendlers
from core.callback_handlers import type_of_work_handlers
from core.message_hendlers import messages_endpoint



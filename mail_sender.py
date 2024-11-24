import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
from dotenv import load_dotenv
import os.path

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

def send_mail(email, subject, text):
    """
    Функция отправки сообщения
    :param email: адрес эл. почты
    :param subject: тема
    :param text: текст письма
    :return: True
    """
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    addr_from = os.getenv('FROM')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')
    port = os.getenv('PORT')

    # формируем сообщение
    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = email
    msg['Subject'] = subject
    body = text
    msg.attach(MIMEText(body, 'plain'))

    # подключаемся к серверу
    server = smtplib.SMTP_SSL(host, int(port))
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()
    return True




message = """

Привет!
Это проверка отправки
почты моим скриптом.
"""
send_mail('agree170766@gmail.com', 'Test', message )
# # список реальных адресов
# mail_list = ['a@b.ru', 'b@c.ru']
#
# count = 0  # глобальный счётчик писем
#
#
#
# load_dotenv(dotenv_path)
# addr_from =os.getenv('FROM')
#
# print(addr_from)


# список реальных адресов
mail_list = ['a@b.ru', 'b@c.ru']

count = 0  # глобальный счётчик писем


def mail_task():
    global count
    send_mail(mail_list[count], 'Проверка', message)
    count += 1


while count < len(mail_list):
    schedule.every(2).seconds.do(mail_task)
    time.sleep(1)  # если нужна доп. задержка

print('Рассылка завершена')
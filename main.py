from flask import Flask, url_for


app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    return 'Привет, я приложение Flask!'

# Статический контент (в папке static/...)
# Все изображения - static/images
# Таблицы стилей - static/css
# Шрифты - static/fonts
# Любые файлы для скачивания
# Файлы JS-сценариев - static/js
# Музыка, видео
#  Функция для удобства пользуемся url_for

# http://127.0.0.1:5000/countdown
@app.route('/countdown')
def countdown():
    cl = ['Старт']
    cl += [str(x) for x in reversed(range(11))]
    cl.append('Финиш')
    return '<br>'.join(cl)

#    """
#    #  мой вариант -рабочий
#    cl = [str(x) for x in reversed(range(11))]
#    return 'start<br>'+'<br>'.join(cl)+ '<br>finish'
#
#    """

# http://127.0.0.1:5000/contacts
@app.route('/contacts')
def contacts():
    return  """
    <b>Контакты</b> mail@maileu.ru <br>
     <b>Телефон</b> Адрес <br>
     <a href='/'> На главную </a> <br>
     <a href='/countdown'> Обратный отсчет </a> <br>
     Телефон
     """
#  http://127.0.0.1:5000/img/1 # обращение в этом случае

# передача параметров в адресной строке
@app.route('/img/<num>') # если явно не указывать тип параметра, то это считается строка
# @app.route('/img/<int:num>') @app.route('/img/<float:num>')
def show_img(num):
    # num += 1 # допустимо при операциях с INT
    """

    :param num: по умолчанию - строка
                <int:num> - целое число
                <float:num> - действительное число
                <path:num> - строка со слешами для URL
                <uuid:num> - идентификатор в 16-м представлении (550e8400-e29b-41d4-a716-446655440000)

    :return:  Путь к картинке
    """
    return f"""    
    <h1>Python logo</h1>
    <img src="{url_for( 'static' , filename= f'images/python-{num}.png')}">
"""
#@app.route('/img')
#def show_img():
#    return f"""
#    <h1>Python logo</h1>
 #   <img src="{url_for( 'static' , filename= 'images/python.png')}">
#"""

#def show_img():
#    return """
#    <h1>Python logo</h1>
#    <img src="./static/images/python.png">"""


#http://127.0.0.1:5000/two-params/Victor/12
@app.route('/two-params/<username>/<int:number>')
def two_params_func(username, number):
    """

    :param username:  # считывет из строки <username>
    :param number: # считывет из строки <int:number>
    :return: html - code - разворачивает в браузере
    """
    param = 100 + number
    return f"""
    <h1>Пользователь  {username}</h1>
    <h2>Номер в системе {number}</h2>
    """


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
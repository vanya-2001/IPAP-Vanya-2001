import json
import os.path
# SECUR_YA sqxdxbtwhdtuzura
from flask import Flask, url_for, request, render_template, redirect, flash
from loginform import LoginForm
from werkzeug.utils import secure_filename


current_directory = os.path.dirname(__file__)  # путь к корню сервера
UPLOAD_FOLDER = f'{current_directory}/static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
# current_directory = os.path.dirname(__file__)  # путь к корню сервера
# UPLOAD_FOLDER = f'{current_directory}/static/uploads'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'svg', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['SECRET_KEY'] = 'too_short_key_too_small_robbery'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/index')
def index():
    param = {}  # словарь с пустым
    param['text'] = 'Этот текст отобразиться на главной странице'  #
    param['title'] = 'Главная'
    #    param['footer'] = '© 2024 Флагман Консалтинг'
    return render_template('index.html', **param)  #
    # * -обращение к списку ** обращение к словарю


#    return """
#    <a href = "/index">Главная</a> |
#    <a href = "/contacts">Контакты</a> |
#    <a href = "/img/1">Картинка 1</a> |
#   <a href = "/img/2">Картинка 2</a> |
#   <a href = "/form_sample">Зарегистрироваться</a>
#    """

# Статический контент (в папке static/...)
# Все изображения - static/images
# Таблицы стилей - static/css
# Шрифты - static/fonts
# Любые файлы для скачивания
# Файлы JS-сценариев - static/js
# Музыка, видео
#  Функция для удобства пользуемся url_for

# http://127.0.0.1:5000/countdown
@app.route('/odd_even/', defaults={'num': 0})
@app.route('/odd_even/<int:num>')
def odd_even(num):
    return render_template('index.html',
                           num=num, title='Четное или нечетное')


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf-8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template(
        'news.html', news=news_list, title='Новости')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('upload.html', title='Выбор файла', form=None)
    #       return render_template('upload.html', title='Выбор файла', form=None)
    elif request.method == 'POST':
        if 'file' not in request.files:
            flash('Файл не был прочитан')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('Файл не был отправлен')
        return redirect(request.url)
    if not allowed_file(file.filename):
        flash('Загрузка файлов данного типа запрещена!')
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('upload.html', title='Файл загружен',
                               form=True)


# @app.route('/pets')
# def pets():
#     with open("pets.json", "rt", encoding="utf-8") as f:
#         pets_info = json.load(f)
#     print(pets_info)
#     return render_template(
#         'pets.html', news=pets_info, title='Питомцы')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return 'Успех'


@app.route('/pets')
def pets():
    with open('OLD/pets.json', 'rt', encoding='utf-8') as f:
        pets_info = json.load(f)
    print(pets_info)
    return render_template('pets.html', pets=pets_info, title='Питомцы')


@app.route('/quene')
def quene():
    return render_template('quene.html', title='Очередь на медосмотр')


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
    return render_template('contacts.html', title='Наши контакты')


@app.route('/about')
def about():
    params = {}
    params['title'] = 'О нас'
    params['text'] = 'Мы перспективная и динамично развивающаяся компания...'
    return render_template('about.html', **params)


#
#  http://127.0.0.1:5000/img/1 # обращение в этом случае

# передача параметров в адресной строке

@app.route('/img/', defaults={'num': None})
@app.route('/img/<num>')
def show_img(num):
    # num += 1
    if num:
        return f"""
        <h1>Python</h1>
        
        <img src="{url_for('static', filename=f'images/python-{num}.png')}">
        <br>
        <a href = "/index">На главную</a>
        """
    else:
        return f"""
                <h1>Здесь ничего нет</h1>
                
                <img src="{url_for('static', filename='images/python.png')}">
                <br>
                <a href = "/index">На главную</a>
                """


# http://127.0.0.1:5000/two-params/Victor/12
# @app.route('/two-params/<username>/<int:number>')
# def two_params_func(username, number):
#     """
#
#     :param username:  # считывет из строки <username>
#     :param number: # считывет из строки <int:number>
#     :return: html - code - разворачивает в браузере
#     """
#     param = 100 + number
#     return f"""
#     <h1>Пользователь  {username}</h1>
#     <h2>Номер в системе {number}</h2>
#     """


# Методы:
# GET - запрашивает информацию с сервера, не меняя его состояния
# POST - отправляет данные на сервер для обработки
# PUT - заменяет текущие данные на сервере данными запроса / like INSERT/
# PATCH - частичная замена данных на сервере / like UPDATE/
# DELETE - удаляет указанные данные

@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('form_sample.html', title='Заполните форму', form='None')
    elif request.method == 'POST':
        return render_template('form_sample.html', tutle='Ваши данные', form=request.form)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')

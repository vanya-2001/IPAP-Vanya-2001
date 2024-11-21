import json

from flask import Flask, url_for, request, render_template

app = Flask(__name__)


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
#
# @app.route('/pets')
# def pets():
#     with open("pets.json", "rt", encoding="utf-8") as f:
#         pets_info = json.load(f)
#     print(pets_info)
#     return render_template(
#         'pets.html', news=pets_info, title='Питомцы')

@app.route('/pets')
def pets():
    with open('pets.json', 'rt', encoding='utf-8') as f:
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


# Методы:
# GET - запрашивает информацию с сервера, не меняя его состояния
# POST - отправляет данные на сервер для обработки
# PUT - заменяет текущие данные на сервере данными запроса / like INSERT/
# PATCH - частичная замена данных на сервере / like UPDATE/
# DELETE - удаляет указанные данные

@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return """
        
        <!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Заполните форму</title>
    <link type="image/png" sizes="32x32" rel="icon" href="images/favicon.png">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link type="text/css" rel="stylesheet" href="css/style.css">

</head>

<body>
<!--главный контейнер-->
<div class="container">
    <h1>Форма для регистрации</h1>
    <form class="login_form" method="post">
        <label for="email">Почта: </label><input class="form-control" type="email" name="email" id="email" placeholder="Введите email">
        <label for="password">Пароль: </label><input class="form-control" type="password" name="password" id="password" >
        <label for="profSelect">Должность на борту нашего рейса</label>
        <select class="form-control" name="profession" id="profSelect">
            <option>Пилот</option>
            <option>Борт-механик</option>
            <option>Радист</option>
            <option>Стюардесса</option>
        </select>
        <button type="submit" class="btn btn-primary">Отправить</button>
    </form>

</div>
<!--главный контейнер (end)-->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
</body>

</html>
<br><a href='/'> На главную </a> 
        """
    elif request.method == 'POST':
        return f"""
        <!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Заполните форму</title>
    <link type="image/png" sizes="32x32" rel="icon" href="images/favicon.png">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link type="text/css" rel="stylesheet" href="css/style.css">

</head>

<body>
<!--главный контейнер-->
<div class="container">
    <h1>Вот что вы отправили</h1>
    <p><b>Ваш email: </b> {request.form['email']}</p>
    <p><b>Пароль: </b> {request.form['password']}</p>
    <p><b>Ваша профессия: </b> {request.form['profession']}</p>
    
    
</div>
<!--главный контейнер (end)-->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
</body>

</html>
<br><a href='/'> На главную </a> 
        """


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')

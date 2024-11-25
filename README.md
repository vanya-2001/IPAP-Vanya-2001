# Проект начинающего верстальщика
## # Основы Python

## Горячие клавиши PyCharm

1.  Чтобы быстро изменить регистр слов с верхнего на нижний, или наоборот,
    используется сочетание клавиш **Ctrl + Shift + U**.

2.  Чтобы исправить ошибки оформления кода, приводя его в соответствие с
    PEP8, используется сочетание клавиш **Ctrl + Alt + L**.

3.  Для оптимизации импортов используется сочетание клавиш **Ctrl + Alt + O**.

4.  В комментировании фрагмента кода поможет сочетание **Ctrl + /**.

5.  Отступы фрагмента кода выставляются клавишей **Tab**, обратный отступ
    **Shift + Tab**.

6.  Для дублирования строк кода применяется сочетание **Ctrl + D**.

7.  Для перемещения блока кода вверх или вниз – сочетание: **Ctrl + Shift +
    \<стрелка\>**

8.  При помощи сочетания клавиш **Ctrl + W**, можно выделить текущий блок, если
    нажимать это сочетание дальше, то будут выделяться родительские блоки.

9.  Если зажать **Ctrl** и кликнуть, например на переменную, то мы попадём в
    блок кода, где эта переменная определена. Тоже самое и с функцией.

10. Удобная команда показа последних блоков кода, с которыми работали: **Ctrl + Shift + E**.

11. "Оборачивание" в нужный оператор осуществляется сочетанием клавиш **Ctrl + Alt + T**.

## Линтеры

**Линтеры** (статические анализаторы кода) – контролируют следование хорошим
практикам кодирования (соблюдения **PEP8** и не только).

Один из популярных линтеров – **Flake 8**.

### Установка:

`$ pip install flake8`

И плагины к нему: **flake8-bugbear** (находит распространённые логические
ошибки) и **pep8-naming** (проверяет имена на соответствие PEP8):

`$ pip install flake8-bugbear pep8-naming`

Интеграция линтера Flake8 в PyCharm

Интеграция проводится следующим образом. Необходимо открыть настройки:

File → Settings → Tools → External Tools и нажать на “+”

В открывшемся окне-форме заполняем поля:

**Name**: Flake8

**Description** (на усмотрение): Линтер хороших практик

Для нахождения пути нужно воспользоваться командой **Bash**: where flake8

Полученный ответ вводим в поле **Program**:
C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python3xx\\Scripts\\flake8.exe
(как пример, путь у Вас будет отличаться)

В поле **Arguments** вводим: `--max-complexity 10 $FileDir$/$FileName$`

В поле **Working Directory**: `$FileDir$`

Далее раскрываем **Advanced Options** и в поле **Output filters** вводим: `$FILE_PATH$:$LINE$`

### Использование

Проверку файла осуществляем нажатием правой кнопкой мыши на нужный файл и далее:

External Tools → Flake8

# Requirements.txt

### Создание

pip freeze > requirements.txt

### Установка

pip install -r requirements.txt

### ORM Filter (Операция - Фильтр)
 * **EQUALS** - query(User).filter(User.name == 'User')
 * **NOT EQUAL** - query(User).filter(User.name != 'User')
 * **LIKE** - query(User).filter(User.name.like('%User%'))
 * **NOT LIKE** - query(User).filter(User.name.notlike('%User%'))
 * **IN** - query(User).filter(User.name.in_(['User1', 'User2', 'User3']))
 * **NOT IN** - query(User).filter(User.name.notin_(['User1', 'User2', 'User3'])) или query(User).filter(~User.name.in_(['User1', 'User2', 'User3'])) 
 * **NULL** - query(User).filter(User.name == None)
 * **AND** - query(User).filter(User.name == 'User', User.id > 3) или query(User).filter(User.name == 'User').filter(User.id > 3)
 * **OR** - query(User).filter((User.name == 'User') | (User.id > 3)) или query(User).filter(or_(User.name == 'User', User.id > 3))

Список источников
http://pythontutor.ru
https://stepik.org/course/67/promo
https://stepik.org/course/512/promo
https://stepik.org/course/431/promo
https://ru.hexlet.io/courses/python_101
https://checkio.org/
https://pythonru.com/uroki/1-vvedenie-vo-flask
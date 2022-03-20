import requests
from flask import Flask, url_for, request
from io import BufferedReader

app = Flask(__name__)


@app.route('/')
def first():
    return "Миссия Колонизация Марса"


@app.route('/promotion')
def promotion():
    result = ['Человечество вырастает из детства.',
              'Человечеству мала одна планета.',
              'Мы сделаем обитаемыми безжизненные пока планеты.',
              'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(result)


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/image_mars')
def image_mars():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!<h1>
                    <img src="/static/img/mars.jpg" alt="здесь должна была быть картинка, но не нашлась">
                    <br>
                    <p1>Вот она какая, красная планета.<p1>
                  </body>
                </html>'''


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                  </head>
                  <body>
                    <h1>Жди нас, Марс</h1>
                    <img src="/static/img/mars.jpg" alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Человечеству мала одной планеты
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Мы сделаем оибитаемыми безжизненные пока планеты
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнём с марса!
                    </div>
                    <div class="alert alert-success" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>"""


@app.route('/selection', methods=['POST', 'GET'])
def selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкета претендента на участие в миссии</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="fullname" class="form-control" id="fullname" aria-describedby="fullnameHelp" placeholder="Ввелите фамилию" name="fullname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="form-check">Какие у вас есть профессии</label>
                                    </div>
                                    <div class="form-group">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="1">
                                        <label class="form-check-label" for="acceptRules">инженер-исследователь</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="2">
                                        <label class="form-check-label" for="acceptRules">пилот</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="3">
                                        <label class="form-check-label" for="acceptRules">строитель</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="4">
                                        <label class="form-check-label" for="acceptRules">экзобиолог</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="5">
                                        <label class="form-check-label" for="acceptRules">врач</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="6">
                                        <label class="form-check-label" for="acceptRules">инженер по терраформированию</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="7">
                                        <label class="form-check-label" for="acceptRules">специалист по радиационной защите</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="8">
                                        <label class="form-check-label" for="acceptRules">астрогеолог</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="9">
                                        <label class="form-check-label" for="acceptRules">гляциолог</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="10">
                                        <label class="form-check-label" for="acceptRules">инженер жизнеобеспечения</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="11">
                                        <label class="form-check-label" for="acceptRules">метеоролог</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="12">
                                        <label class="form-check-label" for="acceptRules">оператор марсохода</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="13">
                                        <label class="form-check-label" for="acceptRules">киберинженер</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="14">
                                        <label class="form-check-label" for="acceptRules">штурман</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="15">
                                        <label class="form-check-label" for="acceptRules">пилот дронов</label>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остатьтся на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form.get('fullname', ''))
        print(request.form.get('name', ''))
        print(request.form.get('email', ''))
        print(request.form.get('class', ''))
        for i in range(1, 16):
            print(request.form.get(str(i), 'off'))
        print(request.form.get('sex', ''))
        print(request.form.get('about', ''))
        print(request.form.get('file', ''))
        print(request.form.get('accept', ''))

        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                  </head>
                  <body>
                    <h1>Моё предложение: {planet_name}</h1>
                    <div>
                      Эта планета близка к Земле
                    </div>
                    <div class="alert alert-primary" role="alert">
                      На ней много необходимо ресурсов
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      На ней есть вода и атмосфера
                    </div>
                    <div class="alert alert-danger" role="alert">
                      На ней есть набольшое магнитное поле
                    </div>
                    <div class="alert alert-success" role="alert">
                      Наконец, она просто красива!
                    </div>
                  </body>
                </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <div>
                      Претендента на участие в миссии {nickname}
                    </div>
                    <div class="alert alert-primary" role="alert">
                      Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    <div>
                      составляет {rating}
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Желаем удачи!
                    </div>
                  </body>
                </html>"""


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Загрузка фотографии для участия в миссии</h1>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="photo">Выберите файл</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <img src="/static/img/img.jpg" alt="">
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        print(f.save('static/img/img.jpg'))
        return "Форма отправлена"


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="/static/img/mars.jpg" alt="First slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="/static/img/mars2.jpg" alt="Second slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="/static/img/mars3.jpg" alt="Third slide">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

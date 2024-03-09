from flask import Flask, render_template, request, make_response, redirect, url_for, flash

# Задание
# 📌 Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# 📌 При отправке которой будет создан cookie файл с данными
# пользователя
# 📌 Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# 📌 На странице приветствия должна быть кнопка "Выйти"
# 📌 При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':        
        for k in request.form.keys():
            if len(request.form.get(k)) == 0:
                return redirect(url_for('index'))
        response = make_response(render_template('logged_in.html', data = request.form))
        for k,v in request.form.items():
            response.set_cookie(k,v)
        return response
    return render_template('index.html')

@app.post('/logout')
def logout():
    response = make_response(redirect(url_for('index')))    
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response



if __name__ == '__main__':
    app.run(debug=True)

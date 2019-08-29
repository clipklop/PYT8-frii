"""
    1) Повторить basic.py
    2) добавить route который принимает 2 числа и возвращает их сумму
    3) добавить route который принимает три строки и возвращает самую длиннную
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return '<br><br><br><br><br><br><b>hello dude!</b>'


@app.route('/post/<int:number>')
def another_home1(number):
    return 'test view {}'.format(number)


@app.route('/sum/<path:string>')
def sum(string):
    x, y = int(string[0]), int(string[1:])
    mysum = x + y
    return 'enter two numbers, {0}, {1}! Ok the SUM is {2}'.format(
        string[0], string[1], str(mysum))


@app.route('/strings/<path:s1>/<path:s2>/<path:s3>')
def three_strings(s1, s2, s3):
    myargs = [s1, s2, s3]
    win = max([len(x) for x in myargs])
    return '{0}<br>{1}<br>{2}<br>Winner: {3}'.format(s1, s2, s3, win)


if __name__ == '__main__':
    app.run()


# @app.route('/<user>')
# @app.route('/<path:user_name>')
# def username(user):
#     return 'hello, user: ' + user

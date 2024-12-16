from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper
    return 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"

@app.route("/username/<name>")
def greet(name):
    return f'Hello there {name + "12"}!'

if __name__ == '__main__':
    app.run(debug=True)
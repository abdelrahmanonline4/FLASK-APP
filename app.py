from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello my name is abdelrahman this is the project 1 test 3 "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

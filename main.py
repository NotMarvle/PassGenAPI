import random
from flask import Flask

lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"

all = lower + upper + numbers + symbols
length = 16
password = "".join(random.sample(all,length))


app = Flask(__name__)

@app.route('/')
def index():
    return "".join(random.sample(all,length))

if __name__ == '__main__':
    app.run()

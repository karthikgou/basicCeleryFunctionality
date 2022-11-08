from celeryCode import app
from time import sleep


@app.task(ignore_result=True)
def add(x, y):
    sleep(30)
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)
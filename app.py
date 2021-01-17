import random
import os
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def _index():
    photo = random.choice(os.listdir("static"))
    id = photo.replace(".jpg", '').replace('id', '')
    return render_template("index.html", photo=photo, id=id)


@app.route("/api")
def _api():
    photo = random.choice(os.listdir("static"))
    return render_template("api.html", photo=photo)


@app.route("/donate")
def _donate():
    return redirect("https://www.tinkoff.ru/rm/ivanov.vladislav82/fLBa057505")


if __name__ == "__main__":
    app.run(port=5050)

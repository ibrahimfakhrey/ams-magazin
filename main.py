from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] ="dasdsada"



@app.route('/')
def home():

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] ="dasdsada"



@app.route('/')
def home():

    return render_template("index.html")

@app.route('/entertainment')
def entertainment():

    return render_template("index.html")
@app.route('/sport')
def sport():

    return render_template("index.html")

@app.route('/education')
def education():

    return render_template("edu.html")

@app.route('/post_details')
def post_details_Copy():

    return render_template("post_details - Copy.html")
@app.route('/post_details')
def post_details():

    return render_template("post_details.html")
@app.route('/post_details')
def post_details2():

    return render_template("post_details - Copy (2).html")
@app.route('/post_details')
def post_details3():

    return render_template("post_details - Copy (3).html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
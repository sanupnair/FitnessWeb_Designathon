from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.secret_key = "secretivekey"
    app.run(debug=True)
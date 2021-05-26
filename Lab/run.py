from flask import Flask, render_template, request, abort, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/aboutme")
def aboutme():
    return app.send_static_file("aboutme.html")

@app.route("/gallery")
def gallery():
    return app.send_static_file('gallery.html')

@app.route("/contact")
def contact():
    return app.send_static_file('contact.html')
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
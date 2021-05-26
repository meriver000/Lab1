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

@app.route('/error_denied')
def error_denied():
    abort(401)

@app.route('/error_internal')
def error_internal():
    return render_template('template.html', name='ERROR 505'), 505

@app.route('/error_not_found')
def error_not_found():
    response = make_response(render_template('template.html', name='ERROR 404'), 404)
    response.headers['X-Something'] = 'A value'
    return response

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
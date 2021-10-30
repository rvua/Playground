from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def index():
    return render_template('index.html', number=3)

@app.route('/play/<int:num>/')
def index_2(num): 
    return render_template('index.html', number=num)

@app.route('/play/<int:num>/<string:color>')
def index_3(num, color):
    return render_template('index.html', number=num, color=color)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
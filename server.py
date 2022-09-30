from turtle import bgcolor
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return redirect ('/play')

@app.route('/play')
def play_default():
    return render_template ('index.html', num=3,bgcolor= "blue")

@app.route('/play/<int:num>')
def play1(num):
    return render_template('index.html', num=num, bgcolor= "blue")

@app.route('/play/<int:num>/<bgcolor>')
def play(num, bgcolor):
    return render_template('index.html',num=num, bgcolor=bgcolor) #attaching html to the function


# return render_template("index.html", phrase="hello", times=5)

if __name__=="__main__":   
    app.run(debug=True) 

from flask import Flask
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html'),

if __name__=='__main__':
    app.run(debug=True, host='localhost', port=5000)
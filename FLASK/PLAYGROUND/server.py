from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def render_play():
    return render_template("index.html", times = 3) 


@app.route('/play/<int:x>')
def repeat_boxes(x):
    x = int((float(x)))
    return render_template("index.html", times = x)


@app.route('/play/<int:x>/<color>')
def render_color(x, color):
    x = int((float(x)))
    return render_template("index.html", times = x, color = color)


if __name__=="__main__":
    app.run(debug=True)

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("playground.html")	# notice the 2 new named arguments!

@app.route('/play')
def render_play():
    if
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)


#@app.route('/play/<x>')


#@app.route('/play/<x>/<color>')


if __name__=="__main__":
    app.run(debug=True)

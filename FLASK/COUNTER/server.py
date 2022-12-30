from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'secret'


@app.route("/")
def index():
    if "visits" not in session:
        session["visits"] = 0
        print(session['visits'])
    else:
        session["visits"] += 1
        print(session['visits'])
    return render_template("index.html")


@app.route("/destroy_session")
def reset_counter():
    session.clear()
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)

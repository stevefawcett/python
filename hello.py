from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Leonora Smells!"

@app.route("/steve")
def steve():
    return render_template('show.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True)

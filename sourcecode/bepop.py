
from flask import Flask, render_template
app = Flask(__name__)

# Root
@app.route("/")
def index():
    return render_template('bepop_main_page.html')

# Main UI
@app.route("/music")
def grid():
    return render_template('main.html')


@app.route("/music/nirvana")
def nirvana():
    return render_template('nirvana.html'), 200

@app.route("/music/kaiser")
def kaiser():
   return render_template('kaiser.html'), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

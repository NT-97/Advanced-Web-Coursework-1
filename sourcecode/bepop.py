
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

@app.route("/music/kaiserchiefs")
def kaiser():
   return render_template('kaiser.html'), 200

@app.route("/music/thekillers")
def killers():
  return render_template('killers.html'), 200

@app.route("/music/elvispressley")
def elvis():
  return render_template('elvis.html'), 200

@app.route("/music/blackeyedpeas")
def blackeyedpeas():
    return render_template('blackeyedpeas.html')


@app.route("/music/theclash")
def theclash():
    return render_template('theclash.html')

@app.route("/music/takethat")
def takethat():
    return render_template('takethat.html')

@app.route("/music/thestoneroses")
def thestoneroses():
    return render_template('thestoneroses.html')

@app.route("/music/michaeljackson")
def michaeljackson():
    return render_template('michaeljackson.html')

@app.route("/music/queen")
def queen():
  return render_template('queen.html')

@app.route("/music/muse")
def muse():
  return render_template('muse.html')

@app.route("/music/coldplay")
def coldplay():
  return render_template('coldplay.html')

@app.route("/music/razorlight")
def razorlight():
  return render_template('razorlight.html')

@app.route("/music/westlife")
def westlife():
  return render_template('westlife.html')

@app.route("/music/greenday")
def greenday():
  return render_template('greenday.html')

@app.route("/music/radiohead")
def radiohead():
  return render_template('radiohead.html')

@app.route("/music/thebeatles")
def thebeatles():
  return render_template('thebeatles.html')

@app.route("/music/oasis")
def oasis():
  return render_template('oasis.html')

#Handles the error if the user goes to a domain that does not exist
@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

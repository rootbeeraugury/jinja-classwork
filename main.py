from flask import Flask, render_template

import utils as util

app = Flask(__name__)

@app.route('/')
def index():
    title = "home :)"
    return render_template("index.html", title=title)

@app.route('/about')
def about():
    title = "about?"
    return render_template("about.html", title=title)

@app.route('/portfolio')
def portfolio():
    title = "portfolio"
    return render_template("portfolio.html", title=title)

@app.route('/contact')
def contact():
    title = "contact me"
    return render_template("contact.html", title=title)

movie_dict = [
  {"title":"Playtime", "genre":"Comedy", "rating":3},
  {"title":"Barbie", "genre":"Comedy", "rating":4},
  {"title":"Night Agent", "genre":"Action", "rating":2},
  {"title":"The Thing", "genre":"Horror", "rating":5},
  {"title":"Pacific Rim", "genre":"Sci-Fi/Action", "rating":5}
]

movie_dict = util.movie_stars(movie_dict)

@app.route('/movies')
def movies():
    context = {
      "title":"cool movies!",
      "movies": movie_dict
    }
    return render_template("movies.html", **context)

app.run(host='0.0.0.0', port=81)

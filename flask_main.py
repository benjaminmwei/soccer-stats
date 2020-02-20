from flask import Flask, render_template, url_for
import importlib
from authors import authors
app = Flask(__name__)


### Mock Content, we will want to get this from a database or files on S3.  
### Jake can author vizes, which we can store in a static folder or on S3.
### Any text can also live in a folder on S3.
posts = [
    {
        'author': 'Lil Pump',
        'title': 'Viz 1',
        'content': 'This is a visualization',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Ramon',
        'title': 'Viz 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'Ramon',
        'title': 'Viz 3',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
        {
        'author': 'Ramon',
        'title': 'Viz 4',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
            {
        'author': 'Ramon',
        'title': 'Viz 4',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
            {
        'author': 'Ramon',
        'title': 'Viz 4',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]
### End Mock Content

@app.route("/")
@app.route("/home")
def home():
    """ Route For Homepage """
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    """ Route for about page """
    return render_template('about.html', title='About', authors = authors)

@app.route("/player_forecast")
def forecast():
    """ Route for forthcoming player and team forecasts"""
    return render_template('forecast.html', title = 'Player Forecast')


if __name__ == '__main__':
    app.run(debug = True)


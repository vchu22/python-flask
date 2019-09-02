from flask import Flask, render_template
app = Flask(__name__)

books = [
  {
    "author": "Jane Shearrion",
    "title": "The Creed of the Ravens",
    "genre": "Fantasy",
    "img":"http://spiritualmilk.com/wp-content/uploads/2017/03/genericBookCover-270x400.jpg",
    "pub_date": "March 17, 2018"
  },
  {
    "author": "Josh Author",
    "title": "2246: Andromeda",
    "genre": "Sci-fi",
    "img":"http://spiritualmilk.com/wp-content/uploads/2017/03/genericBookCover-270x400.jpg",
    "pub_date": "December 30, 2018"
  }
]

@app.route("/")
def home():
  return render_template('home.html', books=books, title="Book Owls")

@app.route("/about")
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)

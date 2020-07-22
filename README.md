# Python Flask

A practice repo for Flask microframework

### Tutorials followed

- LinkedIn Learning: [Full Stack Web Development with Flask](https://www.linkedin.com/learning/full-stack-web-development-with-flask/)

### Run the app

To run a Flask application, make sure you have `flask` installed. If not, execute `pip install Flask` to install it.

Then inside the project folder, run `flask run`.

The `.flaskenv` contains the configurations `FLASK_ENV` for setting environments and `FLASK_APP` for specifying entry-point file.

To turn on debug mode while running the server, make sure you run `export FLASK_DEBUG=1` (in Mac & Linux) or `set FLASK_DEBUG=1` (in Windows) before you start the server. `export FLASK_DEBUG=0` or `set FLASK_DEBUG=0` will turn off your debug mode when running through `flask run`.

Alternatively, you can put `app.run(debug=True)` under the `if __name__ == '__main__':` block in `app.py` and run the server through `python app.py`. That way, your debug mode will depend on the value you set in the `debug` flag. To turn off debug mode when starting your server this way, you will need to set the `debug` to `False`.

### File structure

```
----
 |-- main.py
 |-- application/
      |-- static/   [images, CSS, Javascript]
      |-- templates [For HTML templates]

```

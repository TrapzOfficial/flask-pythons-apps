from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# About page
@app.route('/about')
def about():
    return "<h1>About Page</h1>" #exemple of an basic flask apps keep in mind its not for prod!

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Index Page <h1>'

@app.route('/hello/')
def hello():
    return '<h1> Hello </h1>'

@app.route('/<float:post_id>/')
def show_post(post_id):
    return f'Post {post_id}'

if __name__ == "__main__":
    app.run(debug=True)
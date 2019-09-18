from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Narendra Modi',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Amith Shah',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'Rajnath Singh',
        'title': 'Blog post 3',
        'content': 'Third post content',
        'date_posted': 'April 22, 2018'
    },
    {
        'author': 'Nirmala Ji',
        'title': 'Military operations',
        'content': 'Destory pakistan and get back kashmir',
        'date_posted': 'April 22, 2019'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title="About")


if __name__ == '__main__':
    app.run()

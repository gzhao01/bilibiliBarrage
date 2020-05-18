# from flask import Flask, escape
# app = Flask(__name__)
# app.run(debug=True)

# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello, world'

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % escape(username)

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % escape(subpath)

#========================url_for=====================
# from flask import Flask, escape, url_for

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return '{}\'s profile'.format(escape(username))

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

#======================template=============================
from flask import Flask, render_template
# 引用 APSchedule
from flask_apscheduler import APScheduler
# 引用 congfig 配置
from config import Config, APSchedulerJobConfig

app = Flask(__name__)
app.config.from_object(APSchedulerJobConfig)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
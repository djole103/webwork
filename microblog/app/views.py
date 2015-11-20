from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'Stevie'}
    posts = [ {'author': {'nickname':'BigEasy'},
               'body'  : 'Yeaaaaa'
              },
              {'author': {'nickname': 'Tommy'},
               'body'  : 'Whatever duuude'} ]

    return render_template('index.html',title='Home',user=user,posts=posts)


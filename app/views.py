from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname' : 'Joe'}
	posts = [
		{
			'author': {'nickname' : 'Steven'}, 
			'body' : 'Beautiful day in beach city :)'
		},
		{
			'author': {'nickname' : 'Travis'},
			'body': 'Can\'t wait for the new episode!'
		},
		{
			'author': {'nickname' : 'Mable'},
			'body': 'Where\'s Waddles??'
		}
	]
	title = "All the news unfit to print"
	return render_template('index.html', 
							user=user,
							posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID"%s", remember_me="%s"' %
			(form.open_id.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html',
							title='Sign In',
							form=form,
							providers=app.config['OPENID_PROVIDERS'])
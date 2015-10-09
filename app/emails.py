from .decorators import async
from flask import render_template
from flask.ext.mail import Message
from app import app, mail
from config import ADMINS

@async
def send_async_email(app, msg):
	with app.app_context():
		mail.send(msg)


def send_mail(subject, sender, recipients, text_body, html_body):
	msg = Message(subject, sender=sender, recipients=recipients)
	msg.text = text_body
	msg.html = html_body
	send_async_email(app, msg)

def follower_notification(followed, follower):
	send_email("[microblog] %s is now following you!" % follower.nickname, ADMINS[0], [followed.email],
				render_template("follower_email.txt", follower=follower, followed=followed),
				render_template("follower_email.html", follower=follower, followed=followed))

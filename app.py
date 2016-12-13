from flask import Flask, request
from model import Content, DBSession
import time

app = Flask(__name__)

@app.route('/publish', methods=['GET', 'POST'])
def publish():
	try:
		title = request.form['title']
		content = request.form['content']
		now = int(time.time())
		session = DBSession()
		new_blog = Content(title=title, content=content, time=now)
		session.add(new_blog)
		session.commit()
		session.close()
	except Exception, e:
		app.logger.error(e)
		
	return 'success'

if __name__ == '__main__':
	app.run('127.0.0.1', '9000')

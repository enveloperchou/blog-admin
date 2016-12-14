from flask import Flask, request
from model import Blog, DBSession
import time,json

app = Flask(__name__)

@app.route('/publish', methods=['GET', 'POST'])
def publish():
	try:
		title = request.form['title']
		subtitle = request.form['subtitle']
		description = request.form['description']
		content = request.form['content']
		now = int(time.time())
		session = DBSession()
		new_blog = Blog(title=title, description=description, subtitle=subtitle, content=content, time=now)
		session.add(new_blog)
		session.commit()
		session.close()
	except Exception, e:
		app.logger.error(e)
		
	return 'success'

@app.route('/list')
def list():
	session = DBSession()
	try:
		filter = request.args.get('filter', None)	
		_blogs = []
		if not filter:
			_blogs = session.query(Blog.time).order_by(Blog.time).all()
		else:
			_blogs = session.query(Blog.time).filter(Blog.title.like('%filter%')).all()
			
		blogs = []
		for blog in _blogs:
			blogs.append({'time':blog.time})

		print json.dumps(blogs)
		return json.dumps(blogs) 
	except Exception, e:
		app.logger.error(e)
		return 'error'

@app.route('/blog')
def blog():
	try:
		session = DBSession()
		blog_id = request.args.get('blog_id', 'latest')	
		_blog = None
		if blog_id != 'latest':
			_blog = session.query(Blog).filter(Blog.time == int(blog_id)).one()
		else:
			_blog = session.query(Blog).order_by(Blog.time.asc()).one()
		blog = {'time':_blog.time, 'title':_blog.title, 'description':_blog.description, 'subtitle':_blog.subtitle, 'content':_blog.content}
		print json.dumps(blog)
		return json.dumps(blog)
	except Exception, e:
		app.logger.error(e)
		return 'error'

if __name__ == '__main__':
	app.run('127.0.0.1', '9000')

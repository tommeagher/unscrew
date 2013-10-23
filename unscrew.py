from flask import Flask, make_response, redirect, url_for
from local_settings import SECRET_KEY, SITE_URL

app = Flask(__name__)
#app.config.from_object(__name__)

#redirect the main page
@app.route('/')
def index():
    return(redirect(SITE_URL))

#redirect the Wordpress posts to new site
@app.route('/<int:year>/<int:month>/<path:slug>/')
def posts(year, month, slug):
    return(redirect(SITE_URL+'/blog/{0}/{1}/{2}.html'.format(year, month, slug)))

#redirect the Wordpress pages to the new site
@app.route('/<path:slug>/')
def pages(slug):
    return(redirect(SITE_URL+'/{0}.html'.format(slug)))

#anything that's not caught gets thrown to the 404.
@app.errorhandler(404)
def page_not_found(error):
    return(redirect(SITE_URL+"/404/"))

if __name__ == '__main__':
    #app.debug = True
    app.run()

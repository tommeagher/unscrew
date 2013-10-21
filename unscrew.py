from flask import Flask, make_response, redirect, url_for
from local_settings import SECRET_KEY, SITE_URL

app = Flask(__name__)
#app.config.from_object(__name__)

@app.route('/')
def index():
    return(redirect(SITE_URL))

@app.route('/<int:year>/<path:month>/<path:slug>/')
def posts(year, month, slug):
    return(redirect(SITE_URL+'/blog/{0}/{1}/{2}.html'.format(year, month, slug)))

@app.errorhandler(404)
def page_not_found(error):
    return(redirect(SITE_URL+"/404/"))

if __name__ == '__main__':
    #app.debug = True
    app.run()

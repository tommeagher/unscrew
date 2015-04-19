unscrew
=======

A tiny Flask app to redirect requests from a deprecated WordPress blog URL structure to a new, static site.

This is designed to deploy easily to Heroku. To make it work, you must set a couple of Heroku environment variables (in addition to making sure the URL patterns in the app work for where you want to redirect). You have to set the ```SITE_URL``` and ```SECRET_KEY``` variables. You can do this with the ```heroku config:set ENVVAR``` command.

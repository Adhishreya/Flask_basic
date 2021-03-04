>WSGI-WebServerGatewayInterface
an interface betweent rhe application and the server


> jinja templating
decides the way the data is combined with the template before rendering

venv\Scripts\activate
to activate the environment

## TO create the database
* Activate the environment    `venv\Scripts\activate`
* open shell by typing `python`
* import the schema `from index import db`
* creTE DATABASE USING  `db.create_all()`

## Deployment to heroku
* stay n the virtual environment itself
* in terminal   `heroku login`
* install dependency `pip3 install gunicorn`
* freeze requirements `pip3 freeze > requirements.txt`
* initialize git repository `git init`
* git add `git add.`
* git commit `git commit -m "" `
* create heroku app `heroku create appname`
* `git remote -v`
* `git push heroku master`
* create `Procfile` and type `web:gunicorn` in it
* git add `git add.`
* git commit `git commit -m "" `
* `git push heroku master`

# Solutions to error encountered
* https://devcenter.heroku.com/articles/error-codes#h14-no-web-dynos-running
* https://help.heroku.com/W23OAFGK/why-am-i-seeing-couldn-t-find-that-process-type-when-trying-to-scale-dynos
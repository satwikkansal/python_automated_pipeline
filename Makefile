PROJECT_NAME=autodeploy

setup:
	pip3 install --user -r requirements.txt

prod-run:
	cd $(PROJECT_NAME) && gunicorn --bind 127.0.0.1:5000 app:app 

dev-run:
	export FLASK_ENV=development
	export FLASK_APP=app.py
	cd $(PROJECT_NAME) && flask run

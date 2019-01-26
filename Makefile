PROJECT_NAME=autodeploy

setup:
	pip3 install --user -r requirements.txt

prod-run:
	cd $(PROJECT_NAME) && gunicorn --bind 127.0.0.1:5000 main:app 

dev-run:
	export FLASK_ENV=development
	cd $(PROJECT_NAME) && python main.py

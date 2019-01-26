PROJECT_NAME=autodeploy

setup:
	pip3 install --user -r requirements.txt

prod-run:
	python3 $(PROJECT_NAME)/main.py

run:
	python App.py

setup_run:
	python -m venv env2
	. env/bin/activate
	pip install -r requirements.txt
	python App.py

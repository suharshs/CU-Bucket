all: init deploy

deploy:
	python server.py 8888 mysql://bb3552af18762f:33a8f702@us-cdbr-east-02.cleardb.com/heroku_c75d7e1c93251e5

init:
	pip install -r requirements.txt

db:
	python database/db_setup.py mysql://bb3552af18762f:33a8f702@us-cdbr-east-02.cleardb.com/heroku_c75d7e1c93251e5


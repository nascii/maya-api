IddyBiddy
------
This is a boilerplate of celery(redis)+pyramid+wsgi.

## Run
This project runs fine on python 3. Python 2 is not supported.

To setup a development environment you should:
```
$ cd iddybiddy
$ virtualenv-3.4 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ pip install -e .
```

Also make sure you have redis service running.

If all previous steps passed successfuly you could run http server and celery queue:
```
#1 terminal tab
$ make http
#2 terminal tab(make sure you have activated virtual env)
$ make queue
```

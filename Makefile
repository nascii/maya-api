.PHONY: http queue

http:
	python3 start.py
queue:
	celery worker \
		-A iddybiddy \
		--concurrency=$(shell cat /proc/cpuinfo|grep -F processor | wc -l) \
		--loglevel=info

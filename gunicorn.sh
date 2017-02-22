#!/bin/bash

/home/fauzi/env/bin/gunicorn \
	--workers `/home/fauzi/env/bin/python2.7 -c "import multiprocessing; print multiprocessing.cpu_count() * 2 + 1"` \
	--bind 0.0.0.0:5555 \
	--pid gunicorn.pid \
	'app:create_app("config")'

	#'app.create_app("config")'

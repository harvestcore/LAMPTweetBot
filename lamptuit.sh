#!/bin/bash

function log {
	tail -1 /var/log/apache2/access.log | tr " - - " "\n" | head -1
}

last=$(log)

while true; do
	actual=$(log)

	if [ "$actual" != "$last" ]
	then
		python3.5 ./tweet.py ./es.jpg $actual >> ./data.log
		last=$actual
	fi

	sleep 1
done

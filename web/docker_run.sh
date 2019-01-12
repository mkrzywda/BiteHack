#!/bin/bash
	
	#docker runner 
	echo "Created docker container with id" 
	docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:6.5.4

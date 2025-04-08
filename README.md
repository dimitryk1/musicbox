# musicbox
Creates 2 docker images for ECS: 
--------------------------------
* rockapp - return random rock artist (text), listen for port 9003 or env variable PORT
* operaapp - return random opera artist, listen for port 9002 or env variable PORT
* music box - 
    listen for port 9000 or env variable PORT, 
	using env variables ROCK_HOST and OPERA_HOST (may be IP:port or DNS:port) to call 
	rockapp (route /rock) or operaapp (route /opera) and return their returned values in json format.
	Route /ping will return message "ping successful" in case of success.


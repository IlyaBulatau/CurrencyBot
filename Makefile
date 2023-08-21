up:
	docker compose up -d

stop:
	docker stop $$(docker ps -a -q)
	docker rm $$(docker ps -a -q)

logs:
	docker logs bot -f

psql:
	docker exec -it -u postgres db  psql
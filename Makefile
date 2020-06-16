create_system:
	python3 Scripts/network_generator.py > docker-compose.yml
start_system:
	docker-compose up --build
end_system:
	docker-compose down

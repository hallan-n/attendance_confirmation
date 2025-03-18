build:
	docker build -t attendance_confirmation .

run:
	docker run -d -p 8000:8000 --name attendance_confirmation attendance_confirmation

stop:
    docker stop attendance_confirmation || true

clean:
    docker rm -f attendance_confirmation || true
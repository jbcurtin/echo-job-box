FROM debian:latest

RUN apt-get update && apt-get install python3 -y 
COPY echo.py ./echo.py

ENTRYPOINT python3 ./echo.py

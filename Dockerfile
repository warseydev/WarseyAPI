FROM alpine:latest
COPY src /usr/share/warseyapi/

EXPOSE 5000

WORKDIR /usr/share/warseyapi/

RUN apk add --update python3 py-pip 

RUN pip3 install flask waitress pillow

ENTRYPOINT python3 main.py
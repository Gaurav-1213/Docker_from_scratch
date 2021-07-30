FROM anaconda3:4.10.1
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD python flask_api.py





























#step1 specify base image
#FROM alpine                      # Base OS (Base img) required to run this app is this.
#COPY . /usr/app/						# copy entire content present in this current folder into my docker container
#								# RUN this app on /5000 port only
						# working dir from where we  will start running
											# at last run this file to run the app
# Download and install dependencies
#RUN apk add --update redis

# setup the startuo command
#CMD ["redis-server"]




#FROM python:3.7.5-slim
# FROM python:3.7-alpine as base


#RUN apt-get update -y && \
#    apt-get install -y python-pip python-dev && \
#    apt-get install -y build-essential cmake && \
#    apt-get install -y libopenblas-dev liblapack-dev && \
#    apt-get install -y libx11-dev libgtk-3-dev

#
#COPY ./requirements.txt /requirements.txt
#
#WORKDIR /
#
#RUN pip3 install -r requirements.txt
#
#COPY . /
#
#ENTRYPOINT [ "python3" ]

#CMD [ "rest-server.py" ]

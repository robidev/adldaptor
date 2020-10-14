FROM python:3.7.1-stretch
# FROM python:3-alpine

# Create user that will be used in this image
RUN groupadd -g 1000 appuser && \
     useradd -r -u 1000 -g appuser appuser

LABEL MAINTAINER "Robin Massink <robin.dev@gmail.com>"

WORKDIR /usr/src/app

# Install python libraries
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# the container will be run as this user
USER appuser

# Install the webserver and testscript by copying the api directory
COPY ./server ./server

EXPOSE 10389
ENV PYTHONPATH=/usr/src/app/server
ENV PYTHONUNBUFFERED=1

ENV APPLICATION_NAME        ADLdap
ENV APPLICATION_VERSION     0.0.1
ENV TZ                      Europe/Amsterdam

WORKDIR /usr/src/app/server
CMD ["python3", "server.py","10389"]

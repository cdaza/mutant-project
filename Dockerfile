FROM python:3.9-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
RUN mkdir /flask_app
WORKDIR /flask_app

ADD . /flask_app

# Install production dependencies.
RUN pip install -r requirements.txt

RUN ["chmod", "+x", "/flask_app/entrypoint.sh"]

# Define our command to be run when launching the container
ENTRYPOINT /flask_app/entrypoint.sh
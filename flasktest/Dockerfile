# https://hub.docker.com/r/library/python/tags/
FROM python:3-onbuild  

# Coping source in current directory into the image
# python:3-onbuild expects the source in /usr/src/app
#COPY . /usr/src/app

ADD . /work
WORKDIR /work

COPY api.py .
RUN chmod a+x ./api.py

# Commands in a list
CMD ["python", "api.py"]


FROM python:3.6-jessie

COPY requirements.txt ./
RUN pip install -r requirements.txt


ADD . /work
WORKDIR /work

COPY processhit.py .
COPY app.py .
COPY logging.conf .
RUN chmod a+x ./processhit.py
RUN chmod a+x ./app.py

# https://stackoverflow.com/questions/36014384/docker-fails-to-access-a-gunicorn-served-resource-in-the-host

CMD ["gunicorn", "--log-config", "logging.conf",  "-b", "0.0.0.0:8000",  "app"]


FROM python:3.6-jessie

COPY requirements.txt ./
RUN pip install -r requirements.txt


ADD . /work
WORKDIR /work

COPY ingestproto.py .
RUN chmod a+x ./ingestproto.py


CMD ["python", "./ingestproto.py"]


FROM python:3.6-jessie

COPY requirements.txt ./
RUN pip install -r requirements.txt


ADD . /work
WORKDIR /work

COPY processhit.py .
RUN chmod a+x ./processhit.py


CMD ["python", "./processhit.py"]

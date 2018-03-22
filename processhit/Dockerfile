
FROM python:3.6-jessie

COPY requirements.txt ./
RUN pip install -r requirements.txt


ADD . /work
WORKDIR /work

COPY processhit.py .
COPY app.py .
RUN chmod a+x ./processhit.py
RUN chmod a+x ./app.py

CMD ["gunicorn", "app:api"]

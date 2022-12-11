FROM python:3

WORKDIR /app

ADD . /app/

RUN pip3 install -r requirements.txt

# This should be the ONLY line that's different between dev and prod dockerfiles
CMD python3 server.py

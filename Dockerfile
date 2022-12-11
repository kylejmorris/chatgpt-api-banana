FROM python:3

WORKDIR /app

ADD . /app/

RUN pip3 install -r requirements.txt

RUN playwright install && playwright install-deps

ENV OPENAI_EMAIL="your email"
ENV OPENAI_PASSWORD="your password"

# This should be the ONLY line that's different between dev and prod dockerfiles
RUN python3 server.py

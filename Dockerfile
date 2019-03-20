FROM python:3.7.2-alpine

RUN adduser -D mafApi

WORKDIR /home/mafApi

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY boot.sh ./
RUN chmod a+x boot.sh

USER mafApi

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
FROM python:3.7.2-alpine

RUN adduser -D mafApi

WORKDIR /home/mafApi

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app

USER mafApi

EXPOSE 5000
ENTRYPOINT ["python /app/api.py"]
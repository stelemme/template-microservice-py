FROM python:3.9-alpine

WORKDIR /app
COPY . /app

ENV FLASK_APP=flaskr

RUN pip install --editable .

CMD [ "flask", "run", "--host=0.0.0.0", "--port=3000"]
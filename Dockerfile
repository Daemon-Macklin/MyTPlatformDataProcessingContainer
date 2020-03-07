FROM python:3

RUN mkdir /app

WORKDIR /app

Copy app/ .

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]

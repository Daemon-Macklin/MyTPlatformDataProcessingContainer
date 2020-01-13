FROM python:3

RUN mkdir /app

WORKDIR /app

ADD main.py .
ADD database.py .
ADD rabbitListener.py .
ADD loggerHelper.py .
ADD dataProcessing.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]

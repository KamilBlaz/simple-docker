FROM python:alpine

COPY . /

RUN pip install -r requirements.txt

WORKDIR /src

CMD python3 app.py
  

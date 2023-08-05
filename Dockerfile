FROM python:3.9-slim-bullseye


WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY app.py .

COPY img /app/img

CMD [ "python3", "-m" , "app.py"]

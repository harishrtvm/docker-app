FROM python:3.6
RUN  mkdir /code
COPY . /code/
WORKDIR /code
RUN  pip install -r requirements.txt
EXPOSE 8080
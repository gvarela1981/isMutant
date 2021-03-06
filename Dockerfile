FROM python:3

RUN mkdir -p /my_project

WORKDIR /my_project

COPY app/requirements.txt ./

RUN pip3 install -r requirements.txt

COPY app/src/. .

CMD [ "python3", "./index.py"]
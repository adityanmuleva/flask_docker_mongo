FROM python:3.8

WORKDIR /flask_test

COPY requirements.txt /flask_test/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /flask_test/

EXPOSE 8088

CMD [ "python3", "flask_service.py"]


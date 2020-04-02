FROM python:3.7.3
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src

COPY . /src/

RUN chmod +x /src/cytomine-python-client-script.sh
RUN /src/cytomine-python-client-script.sh

RUN pip install --upgrade pip
COPY requirements.txt /src/
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y curl


CMD  ["gunicorn", "--bind",  "0.0.0.0:80", "api.wsgi"]

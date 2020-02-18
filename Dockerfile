FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /analysis_service
WORKDIR /analysis_service
ADD . /analysis_service/
RUN pip install -r requirements.txt

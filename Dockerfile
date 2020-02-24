FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /analysis_service

ADD . /analysis_service/
RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate


CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]

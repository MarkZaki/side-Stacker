FROM python:3.10


ENV  PYTHONBUFFERED = 1


WORKDIR /app

ADD . .


RUN pip install -r requirments.txt
RUN python manage.py makemigreations
RUN python manage.py migrate


EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
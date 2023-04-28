FROM python:3.10.6

WORKDIR /shortening

COPY . /shortening

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=shortening.settings
ENV PYTHONUNBUFFERED=1

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
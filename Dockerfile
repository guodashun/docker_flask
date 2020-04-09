FROM python:3.6.9-alpine

LABEL maintainer="luckky <luckkywz@gmail.com>" \
	  reference=""

COPY . /app

WORKDIR /app

RUN pip install flask

ENTRYPOINT ["python"]

CMD ["runserver.py"]
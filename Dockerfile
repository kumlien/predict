
FROM python:3.8


# RUN apt-get update -y 
    # && apt-get install -y python3 python3-pip

# RUN apk update \
   # && apk add apk add gcc libc-dev g++ \
   # && apk add --no-cache python3-dev \
   # && pip3 install --upgrade pi

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

ENV FLASK_APP predict
ENV SQLALCHEMY_DATABASE_URI "sqlite:///site.db"
ENV SECRET_KEY 'replace_me'
ENV SQLALCHEMY_TRACK_MODIFICATIONS false

# We copy just the requirements.txt first to leverage Docker cache
# COPY ./Pipfile /app/Pipfile

WORKDIR /app
COPY . /app

RUN pip --no-cache-dir install -r requirements.txt

RUN python 'init_db.py'

EXPOSE 5000

ENTRYPOINT ["python", "run.py"]
# CMD ["run.py"]
# CMD ["python","run.py"]

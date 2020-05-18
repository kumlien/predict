
FROM python:3.8

RUN apt-get update -y \
    && apt-get install -y python3 python3-pip

# RUN apk update \
   # && apk add apk add gcc libc-dev g++ \
   # && apk add --no-cache python3-dev \
   # && pip3 install --upgrade pip

#RUN apt-get update -y && \
#    apt-get install -y python3 python3-pip

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

ENV FLASK_APP predict
# We copy just the requirements.txt first to leverage Docker cache
# COPY ./Pipfile /app/Pipfile

WORKDIR /app
COPY . /app
RUN pip3 --no-cache-dir install -r requirements.txt
RUN python init_db.py

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["run.py"]


# RUN pip3 install pipenv
# RUN pipenv install 


# RUN pipenv shell
# ENTRYPOINT [ "python" ]
# CMD [ "run.py"]
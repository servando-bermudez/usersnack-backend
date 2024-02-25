FROM python:3.12.0-bullseye

# Environment variables
ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV COLUMS 80

# Updateing and Installing server dependencies
RUN apt-get update \
    && apt-get install -y --force-yes \
    nano python3-pip gettext chrpath libssl-dev libxft-dev libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev \
    && rm -rf /var/lib/apt/lists/*

# Defining working directory and adding source code
WORKDIR /app/
COPY config /app/config

# Installing python dependencies
RUN pip install -r config/requirements/development.txt

# Copying project folder
COPY . /app/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
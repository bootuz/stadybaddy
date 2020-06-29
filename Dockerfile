FROM python:3.7
ENV PYTHONUNBUFFERED=1
COPY . /studybuddy/
WORKDIR /studybuddy
RUN pip install -r requirements.txt

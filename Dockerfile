FROM python:3-alpine3.15
WORKDIR /app
COPY . /app
RUN pip3 install Flask
RUN pip3 install numpy
EXPOSE 5000
CMD python ./app.py
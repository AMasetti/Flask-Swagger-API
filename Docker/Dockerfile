FROM python:3.9.9

EXPOSE 5000/udp
EXPOSE 5000/tcp

RUN apt-get update

WORKDIR /usr/src/app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./main.py ./

ENV FLASK_ENV=development
ENV FLASK_APP=main.py

CMD ["flask", "run", "--host", "0.0.0.0"]
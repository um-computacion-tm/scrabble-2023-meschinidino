FROM ubuntu:latest
LABEL authors="dino"

FROM python:3-alpine
RUN apk update
RUN apk add git
RUN git clone https://github.com/um-computacion-tm/scrabble-2023-meschinidino.git
WORKDIR /scrabble-2023-meschinidino
RUN pip install -r requirements.txt

CMD [ "sh", "-c", "git checkout develop", "coverage run -m unittest && coverage report -m && python -m game.main" ]
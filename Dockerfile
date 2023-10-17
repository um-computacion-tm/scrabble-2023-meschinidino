FROM python:3-alpine
LABEL authors="dino"

RUN apk update
RUN apk add git
RUN git clone https://github.com/um-computacion-tm/scrabble-2023-meschinidino.git
WORKDIR /scrabble-2023-meschinidino
RUN git checkout dev
RUN pip install -r requirements.txt

CMD [ "sh", "-c", "coverage run -m unittest && coverage report -m && python -m main" ]
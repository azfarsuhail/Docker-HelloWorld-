FROM python:3.12.3
RUN pip install poetry
LABEL MAINTAINER="AZFAR"
WORKDIR /code
COPY . /code/
RUN poetry install
CMD [ "poetry","run","uvicorn","helloworld.main:app","--host","0.0.0.0" ]
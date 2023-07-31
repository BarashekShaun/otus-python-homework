# To build the image, run "docker build . -t app" in a terminal.
# To run the image, use the command "docker run -p {your port:}8000 -it app"

FROM python:3.9-buster

WORKDIR /app

RUN pip install --upgrade pip setuptools "poetry==1.5.1"
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY . .

CMD uvicorn main:app --host 0.0.0.0 --port 8000
FROM python:3.11.4-bullseye

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . /

RUN chmod +x ./prestart.sh
ENTRYPOINT ["./prestart.sh"]
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]

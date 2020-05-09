FROM python:3-alpine

WORKDIR /app

COPY jankenpon.py ./
COPY tools.py ./
COPY player_classes.py ./
COPY resources.py ./

CMD ["python", "jankenpon.py"]
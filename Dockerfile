FROM python:3-alpine

WORKDIR /app

COPY main.py ./
ADD jankenpon ./jankenpon

CMD ["python", "main.py"]
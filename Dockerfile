FROM python:3-alpine

WORKDIR /app

COPY . jankenpon.py /app/

CMD ["python", "jankenpon.py"]
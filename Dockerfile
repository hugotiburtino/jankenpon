FROM python:3-alpine

WORKDIR /app

COPY jankenpon.py ./

CMD ["python", "jankenpon.py"]
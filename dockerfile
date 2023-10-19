FROM python:3.10.12
WORKDIR /
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code/app
CMD ["uvicorn", "main:app", "--port", "8080"]
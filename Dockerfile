FROM python:3-alpine
RUN apk add --update python3 py3-pip
COPY requirements.txt /src/requirements.txt
RUN pip3 install -r /src/requirements.txt
COPY app.py /src
COPY generator.py /src/generator.py
CMD ["python", "/src/app.py"]

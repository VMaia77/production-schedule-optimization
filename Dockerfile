FROM python:3.9.16
RUN mkdir /solverapi
WORKDIR /solverapi
COPY requirements.txt /solverapi
RUN pip install -r requirements.txt
COPY . /solverapi
EXPOSE 9000
CMD ["python", "main.py"]
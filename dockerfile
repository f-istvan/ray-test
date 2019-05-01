FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ENV SLEEP=3
# ENV EXECUTIONS=4

CMD [ "python", "./app.py" ]

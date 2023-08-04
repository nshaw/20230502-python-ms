FROM python:3.9.17-alpine3.18

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8081

#Add --path $SERVER_SERVLET_CONTEXT_PATH
CMD [ "python", "./app.py"]

FROM python:3.15.0a6-slim
WORKDIR /home/app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python","app.py" ]


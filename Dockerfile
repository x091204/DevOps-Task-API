FROM python:3.11-slim
RUN apt update && apt upgrade -y && apt clean && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
WORKDIR /home/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD [ "python","app.py" ]


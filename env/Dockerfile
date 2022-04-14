FROM python:3.6
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 
COPY . .
EXPOSE 3000
CMD ["python", "app.py"]


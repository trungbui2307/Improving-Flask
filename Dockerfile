FROM python:3.10.5-alpine 

#Set the working directory to /app 
WORKDIR /app
#Copy local contents in to the container  
ADD . /app 
#Install all required dependencies 
RUN pip install -r requirements.txt 
EXPOSE 5000 
CMD ["python", "main.py"]

#docker build -t [name]
#docker run -d -p [port]:[port] [name] 

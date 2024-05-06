FROM python:3.11.9-slim 
#define the base image(python)

WORKDIR /app
# setup the working directory

COPY . .
# RUN chmod 755 /app/data
#COPY data data/
# copy all of contain from the working directory to build the process

RUN apt-get update && apt-get install -y cron 
# install corn for time job
#ffmpeg libgl1 libsm6 libxext6 libxrender-dev

RUN pip install --upgrade pip 
# upgrade pip

# Install all of necessary modules from the requiremen.txt file
RUN pip install -r requirements.txt

RUN chmod 0644 crontab 
# modify the permission on crontab file

RUN crontab crontab 
# start the crontab schedule job

CMD ["cron","-f", "-l", "2"] 
# running corn in the foregraound, 
# beceause it runing in container 
# - debian/ubuntu < cron -f -l 2 >  
# - alpine < crond -f -l 2 > 
# - centos <crond -n>

# CMD python ip_checker.py
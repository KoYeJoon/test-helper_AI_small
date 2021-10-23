FROM python:3.6

WORKDIR /
COPY . .
RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 5000

CMD ["python","-u","app.py"]
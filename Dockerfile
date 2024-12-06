FROM balenalib/jetson-nano-debian-python:latest

WORKDIR ./

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install opencv-python-headless
ADD . ./agri

CMD ["/bin/bash", "./agri/start.sh"]

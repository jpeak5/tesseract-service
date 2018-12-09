FROM jpeak5/tesseract-service:0.1.0
COPY . /opt/
# RUN apt-get update && apt-get -y install python3-pip
RUN pip3 install --upgrade pip
RUN pip install -r /opt/requirements.txt
CMD python3 /opt/app.py
EXPOSE 8888

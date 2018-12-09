FROM tesseractshadow/tesseract4re
COPY . /opt/
RUN apt-get update && apt-get -y install python3-pip
RUN pip3 install -r /opt/requirements.txt
CMD python3 /opt/app.py
EXPOSE 8888

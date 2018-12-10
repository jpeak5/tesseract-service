FROM jpeak5/tesseract-service:0.1.2
COPY . /opt/
CMD python3 /opt/app.py
EXPOSE 8888

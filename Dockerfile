FROM python:3-onbuild
COPY . /opt/
CMD python3 /opt/app.py
EXPOSE 8888

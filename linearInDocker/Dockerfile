FROM python:3
#ADD main.py /
COPY . .
WORKDIR /
RUN pip install -U pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt
CMD ["python", "./main.py"]
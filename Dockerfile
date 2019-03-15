# feel free to change this if you want a different version of opencv or python

FROM jjanzic/docker-python3-opencv

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY cars.py .
COPY src ./src

ENTRYPOINT ["python3", "cars.py"]

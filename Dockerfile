FROM python:3.7

RUN apt-get update
RUN apt-get -y install vim

RUN mkdir /work
WORKDIR /work

RUN pip install --upgrade pip
RUN pip install dash dash_daq plotly pandas jupyter_dash jupyterlab

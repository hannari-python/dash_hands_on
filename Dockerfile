FROM python:3.7

RUN apt-get update
RUN apt-get -y install vim

RUN mkdir /work
WORKDIR /work

RUN pip install --upgrade pip
#RUN pip install dash==0.28.5
#RUN pip install dash-html-components==0.13.2
#RUN pip install dash-core-components==0.35.1
#RUN pip install pandas
#RUN pip install -U scikit-learn
#RUN pip install flask_cors
#RUN pip install --upgrade pip

#RUN pip install click==7.1.1
#RUN pip install cycler==0.10.0
#RUN pip install dash==1.9.1
#RUN pip install dash-bio==0.4.7
#RUN pip install dash-canvas==0.1.0
#RUN pip install dash-core-components==1.8.1
#RUN pip install dash-cytoscape==0.1.1
#RUN pip install dash-daq==0.4.0
#RUN pip install dash-html-components==1.0.2
#RUN pip install dash-renderer==1.2.4
#RUN pip install dash-table==4.6.1
#RUN pip install decorator==4.4.2
#RUN pip install Flask==1.1.1
#RUN pip install Flask-Compress==1.4.0
#RUN pip install future==0.18.2
#RUN pip install imageio==2.8.0
#RUN pip install itsdangerous==1.1.0
#RUN pip install Jinja2==2.11.1
#RUN pip install joblib==0.14.1
#RUN pip install kiwisolver==1.1.0
#RUN pip install MarkupSafe==1.1.1
#RUN pip install matplotlib==3.2.0
#RUN pip install networkx==2.4
#RUN pip install numpy==1.18.1
#RUN pip install pandas==1.0.1
#RUN pip install Pillow==7.0.0
#RUN pip install plotly==4.5.4
#RUN pip install pyparsing==2.4.6
#RUN pip install python-dateutil==2.8.1
#RUN pip install pytz==2019.3
#RUN pip install PyWavelets==1.1.1
#RUN pip install retrying==1.3.3
#RUN pip install scikit-image==0.16.2
#RUN pip install scikit-learn==0.22.2.post1
#RUN pip install scipy==1.4.1
#RUN pip install six==1.14.0
#RUN pip install Werkzeug==1.0.0

RUN pip install dash dash_daq plotly pandas

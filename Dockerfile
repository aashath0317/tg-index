FROM anasty17/mltb:latest
RUN apt-get -qq install -y --no-install-recommends wget unzip
RUN pip3 install --no-cache-dir requirements.txt

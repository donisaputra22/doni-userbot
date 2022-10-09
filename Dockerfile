#kontol

FROM doniuserbot/donibot:doni

RUN git clone -b doni-userbot https://github.com/donisaputra22/doni-userbot /home/doniuserbot/ \
    && chmod 777 /home/doniuserbot \
    && mkdir /home/doniuserbot/bin/

COPY ./sample_config.env ./config.env* /home/doniuserbot/

WORKDIR /home/doniuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]

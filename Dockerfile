#==============×==============#
#      Created by: Kyura-Ex
#=========× Kyuraxp ×=========#

FROM Kyuraxp/kyura-userbot:buster

RUN git clone -b Nande-Telethon https://github.com/donisaputra22/doni-userbot /home/userbot/ \
    && chmod 777 /home/userbot \
    && mkdir /home/userbot/bin/

COPY ./sample_config.env ./config.env* /home/userbot/

WORKDIR /home/userbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]

#==============×==============#
#      Created by: Nande
#=========× Nande ×=========#

FROM nandeuserbot/nandebot:nande

RUN git clone -b doni-userbot https://github.com/donisaputra22/doni-userbot /home/doni-userbot/ \
    && chmod 777 /home/doni-userbot \
    && mkdir /home/doni-userbot/bin/

COPY ./sample_config.env ./config.env* /home/doni-userbot/

WORKDIR /home/doni-userbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]

#==============×==============#
#      Created by: Nande
#=========× Nande ×=========#

FROM nandeuserbot/nandebot:nande

RUN git clone -b doni-userbot https://github.com/donisaputra22/doniuserbot /home/doniuserbot/ \
    && chmod 777 /home/doniuserbot \
    && mkdir /home/doniuserbot/bin/

COPY ./sample_config.env ./config.env* /home/doniuserbot/

WORKDIR /home/doniuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]

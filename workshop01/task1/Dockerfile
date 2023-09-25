FROM python:3.11.5

WORKDIR /python

COPY . .

RUN pip install pip
RUN pip install -r requirements.txt

ENV PORT=5000
ENV INSTANCE_NAME=bear-bear
ENV INSTANCE_HASH=1234657890


# if env variable changes, then this line changes too
EXPOSE ${PORT}

ENTRYPOINT ["sh", "run.sh"]
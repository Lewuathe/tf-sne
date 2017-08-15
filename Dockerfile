FROM tensorflow/tensorflow
MAINTAINER lewuathe

USER root

RUN mkdir -p /srv/tf-sne/
RUN mkdir /srv/tf-sne/data

ADD tf_sne.py /srv/tf-sne
ADD bootstrap.sh /srv/tf-sne
RUN chmod 755 /srv/tf-sne/bootstrap.sh

EXPOSE 6006

WORKDIR /srv/tf-sne

ENTRYPOINT ["./bootstrap.sh"]


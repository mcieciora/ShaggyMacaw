FROM docker:25.0.3-dind-alpine3.19

USER root

RUN apk add openjdk11 git supervisor

COPY ./nodes /root/nodes

COPY supervisord.conf /etc/supervisord.conf
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
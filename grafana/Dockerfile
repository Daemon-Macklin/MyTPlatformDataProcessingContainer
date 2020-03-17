from grafana/grafana

USER root

RUN apk add --no-cache git

RUN git clone https://github.com/JamesOsgood/mongodb-grafana /var/lib/grafana/plugins/

USER grafana
ENTRYPOINT [ "/run.sh" ]

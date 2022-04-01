FROM postgres:14.2

COPY *.sql /docker-entrypoint-initdb.d/
COPY data/*.csv /data/
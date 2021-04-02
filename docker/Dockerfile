FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=tcc

ADD nerdsviajantes_com.sql /docker-entrypoint-initdb.d/

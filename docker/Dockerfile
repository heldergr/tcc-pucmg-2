FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=tcc

# O arquivo nerdsviajantes_com.sql nao esta no repositorio por ser muito grande. 
# Ele pode ser baixado da pasta Learning/tcc-pucmg
ADD nerdsviajantes_com.sql /docker-entrypoint-initdb.d/

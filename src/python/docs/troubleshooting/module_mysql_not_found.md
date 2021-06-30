# Module mysql not found

- Pacote mysql sumiu das libs do virtual env

## Tentativas 

### Tentativa número 1:

- python -m pip install mysqlclient==2.0.3

Erro: 

```
    OSError: mysql_config not found
    mysql_config --version
    mariadb_config --version
    mysql_config --libs
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/3c/df/59cd2fa5e48d0804d213bdcb1acb4d08c403b61c7ff7ed4dd4a6a2deb3f7/mysqlclient-2.0.3.tar.gz#sha256=f6ebea7c008f155baeefe16c56cd3ee6239f7a5a9ae42396c2f1860f08a7c432 (from https://pypi.org/simple/mysqlclient/) (requires-python:>=3.5). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
ERROR: Could not find a version that satisfies the requirement mysqlclient==2.0.3
ERROR: No matching distribution found for mysqlclient==2.0.3
```

### Tentativa número 2 (SUCESSO)

#### Instalar dependências

```terminal
sudo apt-get install libssl-dev gcc python3.8-dev libmysqlclient-dev
```

#### Instalar mysql

```
$ python -m pip install mysql

Collecting mysql
  Using cached mysql-0.0.3-py3-none-any.whl (1.2 kB)
Collecting mysqlclient
  Using cached mysqlclient-2.0.3.tar.gz (88 kB)
Building wheels for collected packages: mysqlclient
  Building wheel for mysqlclient (setup.py) ... done
  Created wheel for mysqlclient: filename=mysqlclient-2.0.3-cp38-cp38-linux_x86_64.whl size=102543 sha256=c74d2bcade53511a8e5c72a7b45a6d1b181637859229ccf50bf34407ecd9b2da
  Stored in directory: /home/helder/.cache/pip/wheels/3a/c1/c3/5a19639a551c921c2c2b39468f4278ce5aa27b4e386a4158e4
Successfully built mysqlclient
Installing collected packages: mysqlclient, mysql
Successfully installed mysql-0.0.3 mysqlclient-2.0.3
```

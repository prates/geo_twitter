# geo_twitter
#### Desenvovido por Alexandre Prates ####

##Arquitetura##

![](https://cloud.githubusercontent.com/assets/482626/20864072/a890d086-b9c8-11e6-88bf-2725afb2f58b.png)

Descrição

Essa aplicação tem como função buscar os tweet armazemnados na base e plot um mapa com as notificações, agrupar essa informações em cluster e mostar as areas com maior incidencia com 
heatmap. Esse projeto tem com dependencia o Redis, foi utilizado via docker, mas você pode instala-lo na máquina local.

Exemplo de inicialização do Redis n máquina local:

```ruby
$ redis-server
```

Exemplo de uso de redis no docker

```ruby
$ docker run --name redis -d -p 6379:6379 redis
```

A implementação e testes foram feito utilizando Ubuntu linux.

Observação
O redis deve estar populado, logo a aplicação coletor deve estar rodando.

##Procedimento de instalação:##

- Crie um diretorio;
- Utilize o virtualenv para criar um container python 2.7

```ruby
$ virtualenv diretorio
```

- Entre no diretorio e copia a pasta do projeto;
- Mude o source do bash para usar a versão do Python instalada no diretorio:
```ruby
$ source bin/activate
```

- Instale as dependencias do python, elas estão no arquivo requiment.txt do projeto. Para instala-las usei o pip:
```ruby
$ pip install -r requeriment.txt
```

- Após instalar vá para a pasta app/plot e execute o twistd para servir os arquivos estaticos:
```ruby
$ twistd -n web -p 8000 --path .
```


- Verifique se o twistd esta funcionando, abra o browser no endereço http://127.0.0.1:9000
- Volte para a pasta geoTwitter.
- Execute o servidor do django:
```ruby
$ python manage.py runserver 0.0.0.0:8001
```

- Abra o navegador na url: http://127.0.0.1:8001/teste/


##Instruções de configuração##
Para configurar o comportamernto da aplicação edite o arquivo app/CONFIG.py


 

This is my first socket project you this make a realtime
sql database but you can use whatever database you want to use
for using this you need to install (python3, pip, virtualenv, docker)
first install dependencies

$ virtualenv modules

than activate or use the routes modules/bin/pip to install the requeriments

know you have all python code that you need to make que sql i use the docker
sql container just run

$ docker pull mysql

$ docker run -p 3306:3306 --name container-name -e MYSQL_ROOT_PASSWORD=your-password -d mysql

than you need and env.py

"connexion": {
      'default': 'local',
      'local': {
          "driver": "mysql",
          "host": "",
          "database": "",
          "user": "",
          "password": "",
          "prefix": ''
          }
  }

than run server for the socket server example_api for the api and client for the client
that will recive the information

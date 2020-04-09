## docker_flask

A simple docker project with python-flask.

### Build

You can build this image by

```
docker build -t example_project_name .
```

or you can get this image on docker hub

```
docker pull guodashun/docker_flask
```

### Run

You need to give a port which you like, for example, *5000*

```
docker run -d -p 5000:1234 guodashun/docker_flask
```

Then you can go to http://127.0.0.1:5000/ in your favorite browser to check it out.


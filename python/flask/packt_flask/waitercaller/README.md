Mongo docker image:
```
$ mkdir ~/data
$ sudo docker run -d -p 27017:27017 -v ~/data:/data/db mongo
```

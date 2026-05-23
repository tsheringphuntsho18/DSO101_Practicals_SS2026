### Removing containers

1. Stop and remove all containers:

```docker
docker stop $(docker ps -q)
docker rm $(docker ps -aq)
```

![image.png](Docker/image%2027.png)

You have to remove the child images (of `node:lts`) before you remove the node image.

1. Run the following command to remove all of the Docker images.

```docker
docker rmi us-east4-docker.pkg.dev/qwiklabs-gcp-02-2075fd19fc7b/my-repository/node-app:0.2
docker rmi node:lts
docker rmi -f $(docker images -aq) # remove remaining images
docker images
```

![image.png](Docker/image%2028.png)

1. Pull the image and run it.

```docker
docker run -p 4000:80 -d us-east4-docker.pkg.dev/qwiklabs-gcp-02-2075fd19fc7b/my-repository/node-app:0.2
```

![image.png](Docker/image%2029.png)

1. Run a curl against the running container.

```docker
curl http://localhost:4000
```

![image.png](Docker/image%2030.png)
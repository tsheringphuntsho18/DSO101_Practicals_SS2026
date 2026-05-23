### **Task 3. Run**

1. Use this code to run containers based on the image you built:

```bash
docker run -p 4000:80 --name my-app node-app:0.1
```

![image.png](Docker/image%209.png)

The `--name` flag allows you to name the container if you like. The `-p` instructs Docker to map the host's port 4000 to the container's port 80. Now you can reach the server at `http://localhost:4000`. Without port mapping, you would not be able to reach the container at localhost.

1. Open another terminal, and test the server:

```bash
curl http://localhost:4000
```

![image.png](Docker/image%2010.png)

The container will run as long as the initial terminal is running. If you want the container to run in the background (not tied to the terminal's session), you need to specify the     `-d` flag.

1. Close the initial terminal and then run the following command to stop and remove the container:

```docker
docker stop my-app && docker rm my-app
```

![image.png](Docker/image%2011.png)

1. Now run the following command to start the container in the background:

```docker
docker run -p 4000:80 --name my-app -d node-app:0.1

docker ps
```

![image.png](Docker/image%2012.png)

1. Notice the container is running in the output of `docker ps`. You can look at the logs by executing `docker logs [container_id]`.

```docker
docker logs [container_id]

## Note: You don't have to write the entire container ID, as long as
## the initial characters uniquely identify the container. 
## For example, you can execute docker logs 17b if the container ID 
## is 17bcaca6f....
```

![image.png](Docker/image%2013.png)

Now modify the application.

1. Edit `app.js` with a text editor of your choice (for example nano or vim) and replace "Hello World" with another string:

![image.png](Docker/image%2014.png)

1. Build this new image and tag it with `0.2`:

```docker
docker build -t node-app:0.2 .
```

![image.png](Docker/image%2015.png)

Notice in Step 1 that you are using an existing cache layer. From Step 2 and on, the layers are modified because you made a change in `app.js`.

1. Run another container with the new image version. Notice how we map the host's port 8080 instead of 80. You can't use host port 4000 because it's already in use.

```docker
docker run -p 8080:80 --name my-app-2 -d node-app:0.2; docker ps
```

![image.png](Docker/image%2016.png)

1. Test the containers:

```docker
curl http://localhost:8080
```

![image.png](Docker/image%2017.png)

1. And now test the first container you made:

```docker
curl http://localhost:4000
```

![image.png](Docker/image%2018.png)
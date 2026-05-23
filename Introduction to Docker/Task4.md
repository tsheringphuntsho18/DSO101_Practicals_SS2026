### **Task 4. Debug**

1. You can look at the logs of a container using `docker logs [container_id]`. If you want to follow the log's output as the container is running, use the `-f` option.

```docker
docker logs -f [container_id]
```

![image.png](Docker/image%2019.png)

Sometimes you will want to start an interactive Bash session inside the running container.
2. You can use `docker exec` to do this. Open another terminal and enter the following command:

```docker
docker exec -it [container_id] bash
```

![image.png](Docker/image%2020.png)

The `-it` flags let you interact with a container by allocating a pseudo-tty and keeping stdin open. Notice bash ran in the `WORKDIR` directory (/app) specified in the  `Dockerfile`. From here, you have an interactive shell session inside the container to debug.

1. You can examine a container's metadata in Docker by using Docker inspect:

```docker
docker inspect [container_id]
```

![image.png](Docker/image%2021.png)

1. Use `--format` to inspect specific fields from the returned JSON. For example:

```docker
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' [container_id]
```

![image.png](Docker/image%2022.png)

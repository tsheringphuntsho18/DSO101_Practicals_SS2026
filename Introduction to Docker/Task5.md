### **Task 5. Publish**

**Push the container to Artifact Registry**

1. Run the command to tag `node-app:0.2`.

```docker
docker build -t us-east4-docker.pkg.dev/qwiklabs-gcp-02-2075fd19fc7b/my-repository/node-app:0.2 .
```

![image.png](Docker/image%2023.png)

1. Run the following command to check your built Docker images.

```docker
docker images
```

![image.png](Docker/image%2024.png)

1. Push this image to Artifact Registry.

```docker
docker push us-east4-docker.pkg.dev/qwiklabs-gcp-02-2075fd19fc7b/my-repository/node-app:0.2
```

![image.png](Docker/image%2025.png)

1. On my-repository, you should see your `node-app` Docker container created:

![image.png](Docker/image%2026.png)
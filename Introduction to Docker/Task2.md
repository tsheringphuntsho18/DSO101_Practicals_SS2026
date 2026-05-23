### **Task 2. Build**

In this section, you will build a Docker image that's based on a simple node application.

1. Execute the following command to create and switch into a folder named `test`.

```bash
mkdir test && cd test
```

1. Create a `Dockerfile`:

![image.png](Docker/image%205.png)

This file instructs the Docker daemon on how to build your image.

- The initial line specifies the base parent image, which in this case is the official Docker image for node version long term support (lts).
- In the second, you set the working (current) directory of the container.
- In the third, you add the current directory's contents (indicated by the `"."` ) into the container.
- Then expose the container's port so it can accept connections on that port and finally run the node command to start the application.

1. Run the following to create the node application:

![image.png](Docker/image%206.png)

This is a simple HTTP server that listens on port 80 and returns "Hello World".

Now build the image.

1. Note again the `"."`, which means current directory so you need to run this command from within the directory that has the Dockerfile:

```bash
docker build -t node-app:0.1 .
```

![image.png](Docker/image%207.png)

The `-t` is to name and tag an image with the `name:tag` syntax. The name of the image is `node-app` and the `tag` is `0.1`. The tag is highly recommended when building Docker images. If you don't specify a tag, the tag will default to `latest` and it becomes more difficult to distinguish newer images from older ones. Also notice how each line in the `Dockerfile` above results in intermediate container layers as the image is built.

1. Now, run the following command to look at the images you built:

```bash
docker images
```

![image.png](Docker/image%208.png)

Notice `node` is the base image and `node-app` is the image you built. You can't remove `node` without removing `node-app` first. The size of the image is relatively small compared to VMs. Other versions of the node image such as `node:slim`  and  `node:alpine` can give you even smaller images for easier portability.
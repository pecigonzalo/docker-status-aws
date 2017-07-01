# Docker Swarm for AWS Status Service
Provides a healthcheck endpoint for the swarm service

*Example project:* **[Terraform docker-swarm](https://github.com/pecigonzalo/tf-docker-swarm)**

### Description
This container will expose and endpoint to be polled for health status by polling the Docker Engine
current swarm status.

### Usage
##### Example
```
docker run -d \
  --name=status-aws \
  --restart=always \
  -p $LOCAL_IP:44554:5000 \
  pecigonzalo/docker-status-aws
```

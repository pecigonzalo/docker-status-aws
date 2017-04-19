docker run \
  --log-driver=json-file \
  --name=status-aws \
  --restart=always \
  -d \
  -p $LOCAL_IP:44554:5000 \
  pecigonzalo/docker-status-aws

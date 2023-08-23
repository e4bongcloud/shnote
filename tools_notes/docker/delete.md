# container
``` bash
docker rm -f $(docker ps -aq)
```
> Only unused containers
``` bash
docker container prune
```

# image
``` bash
docker rmi $(docker images -q)
```

``` bash
docker image rm -f $(docker image ls -q)
```

> Only unused images
``` bash
docker image prune 
```

# volume

``` bash
docker volume prune
```

# all
> unused docker system(container, volume, images, network) delete
``` bash
docker system prune
```

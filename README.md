DHT REST Client

Python REST client developed in flask.
Exposes an enpoint `/temperaturehumidity` that returns the current read of the attached DHT11 sensor on GPIO4

```
docker run -d -p 5000:5000 --device /dev/gpiomem --privileged sensor:latest
```

TODOs:
- properly setup privileges to avoid running the container in privileged mode (makes it safer and swarm-friendly)
- allow automated build on upstream container. currently is locally built and pushed to remote.
- cache readings to prevent DHT saturation. This will require background cache refresh. All the thing in a raspberry pi zero GPIO is slow 


# Welcome to URL Lookup
## To run:
        docker-compose build
        docker-compose up

## To use:
        curl localhost:80/
        curl localhost:80/urlinfo/1/<hostname:port>/<path>

## To test:
        pytest .

## To do:
        grep -irn TODO
* Add typing
* Add more tests
* Make Datastore a real ABC
* Insert data into Redis only once
* Set this all up with helm instead of docker-compose
  * https://github.com/helm/charts/tree/master/stable/redis-ha
* Enable redis sentinel for HA etc. via above
* Enable autoscaling of app server nodes
* Put a gateway on it

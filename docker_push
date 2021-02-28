#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push dansonio/savannah-orders_orders_app
docker push dansonio/savannah-orders_comms_worker

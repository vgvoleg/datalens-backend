#!/bin/sh
docker run --rm -it -v /Users/40in/dev/packer/cloud-deploy/dashboard/:/data/ -e GRAFANA_OAUTH_TOKEN="$GRAFANA_OAUTH_TOKEN" cr.yandex/crp6ro8l0u0o3qgmvv3r/dashboard:latest java -jar build/java-dashboard.jar upload /data/duty.yaml
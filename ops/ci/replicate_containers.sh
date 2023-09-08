#!/usr/bin/env bash

set -eux

pull_push () {
    if ! docker manifest inspect $2 > /dev/null; then
        echo "Replicating image from $1 to $2"
        docker pull $1
        docker image tag $1 $2
        docker push $2
    else
        echo "Image $2 already pushed, skip"
    fi
}

echo "mirroring service images"

US_SRC="registry.yandex.net/data-ui/united-storage:latest"
US_DST="cr.yandex/$DOCKER_REGISTRY_YC_EXT/united-storage:latest"
pull_push $US_SRC $US_DST

S3_SRC="registry.yandex.net/statinfra/s3cloudserver@sha256:b53e57829cf7df357323e60a19c9f98d2218f1b7ccb1d7cea5761a5a227a9ee3"
S3_DST="cr.yandex/$DOCKER_REGISTRY_YC_EXT/s3cloudserver"
pull_push $S3_SRC $S3_DST

CH_22_SRC="registry.yandex.net/statinfra/clickhouse-server:22.11"
CH_22_DST="cr.yandex/$DOCKER_REGISTRY_YC_EXT/clickhouse-server:22.11"
pull_push $CH_22_SRC $CH_22_DST

CH_22_3_SRC="registry.yandex.net/statinfra/clickhouse-server@sha256:74e094253baa15b18ec1ea3a79fb4015451de3bb23c40c99dcc37d1f85c1ac09"
CH_22_3_DST="cr.yandex/$DOCKER_REGISTRY_YC_EXT/clickhouse-server:22.3"
pull_push $CH_22_3_SRC $CH_22_3_DST

MYSQL_SRC="registry.yandex.net/statinfra/mysql@sha256:d8e4032005f53a774f2361281ebf61fa3d7635d5dacf9c58bc54e823ddcf9f1d"
MYSQL_DST="cr.yandex/$DOCKER_REGISTRY_YC_EXT/mysql:5.6"
pull_push $MYSQL_SRC $MYSQL_DST

MYSQL_8012_SRC="registry.yandex.net/statinfra/mysql@sha256:574bf8a61e3276788bcaa9a9e226977ea3037f439295e2a07b624b8aaebd66d4"
MYSQL_8012_DST="cr.yandex/$DOCKER_REGISTRY_YC_EXT/mysql:8.0.12"
pull_push $MYSQL_8012_SRC $MYSQL_8012_DST

INIT_DB_SRC="registry.yandex.net/statinfra/base/bi/initdb@sha256:41477e01d5e1017d31c09776ded1b135ce7e58add715a024fc294c0490b95c44"
INIT_DB_DST="cr.yandex/$DOCKER_REGISTRY_YC_EXT/initdb:41477"
pull_push $INIT_DB_SRC $INIT_DB_DST

INIT_DB_LATEST_SRC="registry.yandex.net/statinfra/base/bi/initdb:latest"
INIT_DB_LATEST_DST="cr.yandex/$DOCKER_REGISTRY_YC_EXT/initdb:latest"
pull_push $INIT_DB_LATEST_SRC $INIT_DB_LATEST_DST

# access denied, copy by hand
#YDB_SRC="registry.yandex.net/yandex-docker-local-ydb@sha256:882755b316b72490702e372e82c84df770b046fd3ecdd77163fc088a82c043a1"
#YDB_DST="cr.yandex/$DOCKER_REGISTRY_YC_EXT/yandex-docker-local-ydb:882755"
#pull_push $YDB_SRC $YDB_DST
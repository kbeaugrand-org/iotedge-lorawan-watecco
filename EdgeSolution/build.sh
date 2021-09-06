#!/bin/sh

image_name=kbeaugrand/az-iotedge-watteco-decoder-module
tag_name=0.0.1
module_path="./modules/WattecoStandardReportDecoderModule"

docker build --rm -f "${module_path}/Dockerfile.amd64"      -t "${image_name}:${tag_name}-amd64" $module_path
docker build --rm -f "${module_path}/Dockerfile.arm32v7"    -t "${image_name}:${tag_name}-arm32v7" $module_path
docker build --rm -f "${module_path}/Dockerfile.arm64v8"    -t "${image_name}:${tag_name}-arm64v8" $module_path

docker push "${image_name}:${tag_name}-amd64"
docker push "${image_name}:${tag_name}-arm32v7"
docker push "${image_name}:${tag_name}-arm64v8"

docker manifest create $image_name:$tag_name \
        --amend $image_name:$tag_name-amd64 \
        --amend $image_name:$tag_name-arm32v7 \
        --amend $image_name:$tag_name-arm64v8

docker push $image_name:$tag_name
#!/bin/bash

# Load environment variables from .env file
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
else
    echo "Error: .env file not found. Please create it from .env.example"
    exit 1
fi

# Build the full image name
IMAGE_NAME="${DOCKER_REGISTRY}/${DOCKER_USERNAME}/${DOCKER_REPOSITORY}/${DOCKER_IMAGE_NAME}:latest"

echo "Pushing image: ${IMAGE_NAME}"

# Push the image
docker push "${IMAGE_NAME}"


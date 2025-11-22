#!/bin/bash

# Load environment variables from .env file
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
else
    echo "Error: .env file not found. Please create it from .env.example"
    exit 1
fi

# Login to GitHub Container Registry
if [ -z "$GITHUB_TOKEN" ]; then
    echo "Error: GITHUB_TOKEN not set in .env file"
    echo "Please add GITHUB_TOKEN=your-token to your .env file"
    exit 1
fi

echo "Logging in to ${DOCKER_REGISTRY} as ${DOCKER_USERNAME}..."
echo "$GITHUB_TOKEN" | docker login "${DOCKER_REGISTRY}" -u "${DOCKER_USERNAME}" --password-stdin


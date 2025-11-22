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

echo "Verifying image: ${IMAGE_NAME}"
echo ""

# Method 1: Check if image exists locally
echo "1. Checking local Docker images:"
if docker images "${IMAGE_NAME}" --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}\t{{.CreatedAt}}" | grep -q "${DOCKER_IMAGE_NAME}"; then
    docker images "${IMAGE_NAME}" --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}\t{{.CreatedAt}}"
    echo "✓ Image found locally"
else
    echo "✗ Image not found locally"
fi

echo ""
echo "2. Checking remote registry (requires authentication):"

# Method 2: Try to pull manifest (this verifies it exists remotely)
if docker manifest inspect "${IMAGE_NAME}" > /dev/null 2>&1; then
    echo "✓ Image exists in remote registry!"
    echo ""
    echo "Image details:"
    docker manifest inspect "${IMAGE_NAME}" | grep -E '"mediaType"|"size"|"digest"' | head -3
    echo ""
    echo "View on GitHub:"
    echo "https://github.com/${DOCKER_USERNAME}?tab=packages"
else
    echo "✗ Could not verify image in remote registry"
    echo "  This might mean:"
    echo "  - Image doesn't exist yet"
    echo "  - You need to login: ./docker-login.sh"
    echo "  - Image name is incorrect"
fi

echo ""
echo "3. Alternative: Check GitHub Packages page:"
echo "   https://github.com/${DOCKER_USERNAME}?tab=packages"
echo "   or"
echo "   https://github.com/users/${DOCKER_USERNAME}/packages/container/${DOCKER_REPOSITORY}%2F${DOCKER_IMAGE_NAME}"


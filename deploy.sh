#!/bin/bash

set -e  

source .env

echo "🔨 Building Docker image: $IMAGE_NAME ..."
docker build -t $IMAGE_NAME .

echo "🔐 Authenticating with Google Artifact Registry..."
gcloud auth configure-docker $REGION-docker.pkg.dev

echo "📤 Pushing image to Artifact Registry..."
docker push $IMAGE_NAME

echo "🚀 Deploying to Cloud Run..."
gcloud run deploy $SERVICE_NAME \
    --image $IMAGE_NAME \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated \
    --port 8080 \
    --memory 2Gi \
    --set-env-vars SCRAPED_DATA_PATH=$SCRAPED_DATA_PATH,POST_PROCESSED_DATA_PATH=$POST_PROCESSED_DATA_PATH,URL=$URL

echo "✅ Deployment completed successfully!"
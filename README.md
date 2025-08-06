# DevOps + Cloud Project: FastAPI CI/CD with Docker and Azure

This is a basic starter project to deploy a FastAPI app using Docker, GitHub Actions, and Azure Web App for Containers.

## Tech Stack
- FastAPI
- Docker
- GitHub Actions
- Azure Web App

## Quickstart
1. Clone the repo
2. Build Docker image: `docker build -t myapp .`
3. Run locally: `docker run -p 80:80 myapp`
4. Push to GitHub
5. Set up GitHub Secrets:
    - `AZURE_APP_NAME`
    - `AZURE_WEBAPP_PUBLISH_PROFILE`
6. GitHub Actions will auto-deploy on push
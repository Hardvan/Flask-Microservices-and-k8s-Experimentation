# Flask Microservices & k8s Experimentation

This project demonstrates how to create and deploy 5 Flask microservices on Kubernetes (k8s). The microservices (`Service A`, `Service B`, `Service C`, `Service D`, and `Service E`) communicate with each other within the k8s cluster. The setup involves Dockerizing the Flask applications and deploying them on Kubernetes.

## Table of Contents

- [Flask Microservices \& k8s Experimentation](#flask-microservices--k8s-experimentation)
  - [Table of Contents](#table-of-contents)
  - [Project Structure](#project-structure)
  - [Prerequisites](#prerequisites)
  - [Microservice Overview](#microservice-overview)
  - [Setup Guide](#setup-guide)
    - [Step 1: Dockerize the Flask Services](#step-1-dockerize-the-flask-services)
    - [Step 2: Build and Push Docker Images](#step-2-build-and-push-docker-images)
    - [Step 3: Deploy Services on Kubernetes](#step-3-deploy-services-on-kubernetes)
    - [Step 4: Port Forward for Local Testing](#step-4-port-forward-for-local-testing)
  - [Testing the Application](#testing-the-application)
  - [Cleaning Up](#cleaning-up)

---

## Project Structure

```plaintext
    📂 Service A
        - app_a.py                          # Flask application for Service A
        - Dockerfile                        # Dockerfile for Service A
    📂 Service B
        - app_b.py                          # Flask application for Service B
        - Dockerfile                        # Dockerfile for Service B
    📂 Service C
        - app_c.py                          # Flask application for Service C
        - Dockerfile                        # Dockerfile for Service C
    📂 Service D
        - app_d.py                          # Flask application for Service D
        - Dockerfile                        # Dockerfile for Service D
    📂 Service E
        - app_e.py                          # Flask application for Service E
        - Dockerfile                        # Dockerfile for Service E
    📂 k8s
        - deployment_service_a.yaml         # Kubernetes Deployment YAML for Service A
        - deployment_service_b.yaml         # Kubernetes Deployment YAML for Service B
        - deployment_service_c.yaml         # Kubernetes Deployment YAML for Service C
        - deployment_service_d.yaml         # Kubernetes Deployment YAML for Service D
        - deployment_service_e.yaml         # Kubernetes Deployment YAML for Service E
- README.md                                 # This README file
- service_a_loadbalancer.yaml               # Kubernetes Service LoadBalancer configuration for Service A
```

## Prerequisites

- Docker
- Kubernetes
- kubectl
- Python 3.x
- A Docker Hub account (or any other container registry, optional)

## Microservice Overview

- **Service A**: Main service that communicates with other services.
- **Service B**: Returns a simple message to Service A.
- **Service C**: Returns a different message to Service A.
- **Service D**: Returns some status to Service A.
- **Service E**: Processes some data and responds to Service A.

## Setup Guide

### Step 1: Dockerize the Flask Services

Each microservice (Service A, B, C, D, and E) has its own Dockerfile. Build Docker images for these services.

For `Service A`:

```bash
cd Service\ A
docker build -t flask-service-a:latest .
```

For `Service B`:

```bash
cd Service\ B
docker build -t flask-service-b:latest .
```

For `Service C`:

```bash
cd Service\ C
docker build -t flask-service-c:latest .
```

For `Service D`:

```bash
cd Service\ D
docker build -t flask-service-d:latest .
```

For `Service E`:

```bash
cd Service\ E
docker build -t flask-service-e:latest .
```

### Step 2: Build and Push Docker Images

If you want to push the images to a container registry (e.g., Docker Hub), first tag and push them.

```bash
docker tag flask-service-a:latest <your_dockerhub_username>/flask-service-a:latest
docker push <your_dockerhub_username>/flask-service-a:latest

docker tag flask-service-b:latest <your_dockerhub_username>/flask-service-b:latest
docker push <your_dockerhub_username>/flask-service-b:latest

docker tag flask-service-c:latest <your_dockerhub_username>/flask-service-c:latest
docker push <your_dockerhub_username>/flask-service-c:latest

docker tag flask-service-d:latest <your_dockerhub_username>/flask-service-d:latest
docker push <your_dockerhub_username>/flask-service-d:latest

docker tag flask-service-e:latest <your_dockerhub_username>/flask-service-e:latest
docker push <your_dockerhub_username>/flask-service-e:latest
```

If you're using local Docker images with Minikube or a local cluster, you can skip pushing them.

### Step 3: Deploy Services on Kubernetes

Deploy the microservices using the Kubernetes deployment YAML files.

```bash
kubectl apply -f k8s/
```

This will deploy all services (A to E) onto the Kubernetes cluster.

### Step 4: Port Forward for Local Testing

After deploying the services, use `kubectl port-forward` to access them locally.

To forward `Service A` to your local machine:

```bash
kubectl get pods                          # Get the pod name for Service A
kubectl port-forward <service-a-pod-name> 8080:5000
```

You can do similar port forwarding for other services (e.g., `Service B`, `Service C`, etc.) if you need to test them directly.

## Testing the Application

After port forwarding, test `Service A` by making a request to:

```bash
curl http://localhost:8080/service_a
```

`Service A` will internally call `Service B`, `Service C`, `Service D`, and `Service E`, and you should see a JSON response like this:

```json
{
  "service": "A",
  "response_from_b": {
    "service": "B",
    "message": "Hello from Service B"
  },
  "response_from_c": {
    "service": "C",
    "message": "Hello from Service C"
  },
  "response_from_d": {
    "service": "D",
    "status": "Service D is healthy"
  },
  "response_from_e": {
    "service": "E",
    "processed_data": "Data from Service E"
  }
}
```

## Cleaning Up

To delete the Kubernetes deployments and services:

```bash
kubectl delete -f k8s/
kubectl delete -f service_a_loadbalancer.yaml  # If used
```

This will remove all microservices from your Kubernetes cluster.

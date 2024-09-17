# Flask Microservices & k8s Experimentation

This project demonstrates how to create and deploy Flask microservices on Kubernetes (k8s). The microservices (`Service A` and `Service B`) communicate with each other within the k8s cluster, with `Service A` making internal requests to `Service B`. The setup involves Dockerizing the Flask applications and deploying them on Kubernetes.

## Table of Contents

- [Flask Microservices \& k8s Experimentation](#flask-microservices--k8s-experimentation)
  - [Table of Contents](#table-of-contents)
  - [Project Structure](#project-structure)
  - [Prerequisites](#prerequisites)
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
    📂 k8s
        - deployment_service_a.yaml         # Kubernetes Deployment YAML for Service A
        - deployment_service_b.yaml         # Kubernetes Deployment YAML for Service B
- README.md                                 # This README file
- service_a_loadbalancer.yaml               # Kubernetes Service LoadBalancer configuration for Service A
```

## Prerequisites

- Docker
- Kubernetes
- kubectl
- Python 3.x
- A Docker Hub account (or any other container registry, optional)

## Setup Guide

### Step 1: Dockerize the Flask Services

Each microservice (Service A and Service B) has its own Dockerfile. Build Docker images for these services.

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

### Step 2: Build and Push Docker Images

If you want to push the images to a container registry (e.g., Docker Hub), first tag and push them.

```bash
docker tag flask-service-a:latest <your_dockerhub_username>/flask-service-a:latest
docker push <your_dockerhub_username>/flask-service-a:latest

docker tag flask-service-b:latest <your_dockerhub_username>/flask-service-b:latest
docker push <your_dockerhub_username>/flask-service-b:latest
```

If you're using local Docker images with Minikube or a local cluster, you can skip pushing them.

### Step 3: Deploy Services on Kubernetes

Deploy the microservices using the Kubernetes deployment YAML files.

Apply the deployment configurations for Service A and Service B:

```bash
kubectl apply -f k8s/
```

### Step 4: Port Forward for Local Testing

After deploying the services, use `kubectl port-forward` to access them locally.

To forward `Service A` to your local machine:

```bash
kubectl get pods                          # Get the pod name for Service A
kubectl port-forward <service-a-pod-name> 8080:5000
```

To forward `Service B` (if needed):

```bash
kubectl get pods                          # Get the pod name for Service B
kubectl port-forward <service-b-pod-name> 8081:5001
```

Now, you can access Service A at `http://localhost:8080/service_a`, and it will make internal calls to Service B.

## Testing the Application

After port forwarding, test `Service A` by making a request to:

```bash
curl http://localhost:8080/service_a
```

You should receive a JSON response with data from both `Service A` and `Service B`:

```json
{
  "service": "A",
  "response_from_b": {
    "service": "B",
    "message": "Hello from Service B"
  }
}
```

## Cleaning Up

To delete the Kubernetes deployments and services:

```bash
kubectl delete -f k8s/deployment_service_a.yaml
kubectl delete -f k8s/deployment_service_b.yaml
kubectl delete -f service_a_loadbalancer.yaml  # If used
```

This will remove the microservices from your Kubernetes cluster.

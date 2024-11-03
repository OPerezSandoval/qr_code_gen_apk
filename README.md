# QR Code Generator - Deployed with Kubernetes utilizing Minikube

This repository contains the code and configuration files to deploy a QR code generator application using Kubernetes in a Minikube environment.

## Prerequisites

- **Docker**: Required by Minikube to run containers. Install Docker [here](https://docs.docker.com/get-docker/).
- **Minikube**: Install Minikube [here](https://minikube.sigs.k8s.io/docs/start/).
- **kubectl**: The Kubernetes command-line tool. Install kubectl [here](https://kubernetes.io/docs/tasks/tools/).

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/OPerezSandoval/qr_code_gen_apk.git
cd qr-code-generator
```

### 2. Start Minikube

After Minikube is installed, start it 

```bash
minikube start --driver=docker 
docker ps 
```
If Minikube is already installed and configured, this will start the Kubernetes cluster locally. You can verify that the docker container is running with docker ps command.

### 3. Deploy the Application to Kubernetes


Use the provided Kubernetes manifests to deploy the application. You will need to add the correct image inside the `deploy.yaml` file.

```
operez11/qr-code-generator:latest 
```

#### **Apply the Deployment and Service Manifests**

```bash
cd kube
kubectl apply -f .
```

These commands will:
- Deploy your application with a Kubernetes `Deployment`.
- Expose it via a `Service` so it can be accessed.

### 4. Verify Deployment

Check if the pods are running successfully.

```bash
kubectl get pods
```

You should see the pods listed as `Running`.

### 5. Access the Application

Since Minikube uses NodePort services to expose applications, you can retrieve the URL to access the service.

```bash
minikube service qr-code-service --url
```

Copy the output URL and open it in your browser. This URL should take you to the QR code generator application.

---

## Stopping Minikube

Once you’re done, you can stop the Minikube cluster with:

```bash
minikube stop
```

To delete the Minikube cluster entirely:

```bash
minikube delete
```

---

## Additional Documentation

- [Minikube Documentation](https://minikube.sigs.k8s.io/docs/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)

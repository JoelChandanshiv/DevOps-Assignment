# 🚀 DevOps Assignment – Two-Tier Web App with Full CI/CD on AWS

Welcome to my DevOps Assignment project! This repository contains a **fully automated, production-ready two-tier web application** built using:

- ✅ FastAPI (Python) for the backend
- ✅ Next.js (React) for the frontend
- ✅ Docker + GitHub Actions for CI/CD
- ✅ AWS ECS Fargate + ALB for hosting
- ✅ Terraform for Infrastructure as Code
- ✅ CloudWatch for monitoring
- ✅ Secrets Manager and IAM for security

> 🔗 [Live Frontend URL](http://your-alb-url) | 🔗 [Live Backend URL](http://your-alb-url/api/message)  
> 📽️ [Watch the Demo Video](https://link-to-demo-video)  
> 🗺️ [View Full Architecture Diagram](https://joelchandanshiv.github.io/DevOps-Assignment/architecture.html)


---

## 📌 Project Overview

This project demonstrates an end-to-end DevOps pipeline by building, testing, containerizing, deploying, and operating a full-stack web application on AWS. It showcases modern DevOps practices including:

- Automated CI/CD workflows using GitHub Actions
- Containerization using Docker
- Image versioning and storage using AWS ECR (Elastic Container Registry)
- Cloud-native deployment on AWS ECS Fargate with ALB
- Infrastructure provisioning with Terraform (IaC)
- Monitoring and alerting via AWS CloudWatch and SNS
- Secure secret management using AWS Secrets Manager


---

## 🏗️ Architecture Overview

![Architecture Diagram](https://raw.githubusercontent.com/JoelChandanshiv/DevOps-Assignment/main/docs/architecture_screenshot.jpeg)

> Or explore the [interactive architecture diagram](https://joelchandanshiv.github.io/DevOps-Assignment/architecture.html)

### Key Components:
- **Frontend**: Next.js app deployed on ECS Fargate
- **Backend**: FastAPI app with `/health` and `/api/message` endpoints
- **Load Balancer**: ALB with path-based routing
- **Monitoring**: CloudWatch dashboard + SNS alerts
- **Security**: IAM roles, Secrets Manager, and network restrictions
- **Infrastructure**: Terraform-managed with S3 backend and DynamoDB lock table

---

## ⚙️ Features & Stack

| Feature | Description |
|--------|-------------|
| 🐳 Dockerized | Multi-stage Dockerfiles for both frontend & backend |
| 🔁 GitHub Actions | CI/CD workflows for test → build → push → deploy |
| 🌐 ALB Routing | Path-based routing to backend/frontend |
| 🔒 Security | IAM roles, AWS Secrets Manager, security groups |
| 📊 Monitoring | CloudWatch dashboards, alarms, SNS alerts |
| 🧪 Testing | 2 unit tests (backend) + 2 e2e tests (frontend) |
| 🧱 Infrastructure | 100% Terraform: ECS, VPC, ALB, IAM, Secrets, CloudWatch |
| ♻️ Git SHA Tagging | Docker images tagged using GitHub SHA |

---

## 🔁 Git Workflow

- `main`: Production-ready code – triggers deployment
- `develop`: Integration branch – triggers CI builds & tests
- Docker images are tagged with Git SHA: `your-repo-name:<GIT_SHA>`

---

## 🔄 CI/CD Pipeline

### ✅ `develop` Branch:
- Lint + run backend unit tests
- Run frontend e2e tests
- Build Docker images (multi-stage)
- Tag with Git SHA
- Push to AWS ECR

### 🚀 `main` Branch:
- Trigger `terraform apply`
- Update ECS task definitions
- Roll out updated services with ALB health checks

---

## 🧑‍💻 Local Setup Instructions

### Prerequisites:
- AWS CLI configured
- Terraform installed
- GitHub CLI (optional)

### 1. Clone the Repository
```bash
git clone https://github.com/JoelChandanshiv/DevOps-Assignment.git
cd DevOps-Assignment
```

### 2. Run Locally

### Backend

```bash
cd backend
docker build -t backend .
docker run -p 8000:8000 backend
```

### Frontend

```bash
cd frontend
docker build -t frontend .
docker run -p 3000:3000 frontend
```

## ☁️ Deployment on AWS

### 1. Terraform Initialization

```bash
cd terraform
terraform init
terraform apply -var-file="terraform.tfvars"
```

> 💡 **Tip:**  Ensure `terraform.tfvars` includes your AWS region, ECR image tags, VPC CIDRs, and any other required variables.

### 2. Secrets Setup

- Store your API keys and secrets in AWS Secrets Manager.

- These will be injected into ECS tasks automatically via environment variables defined in the Terraform configuration.

## 📊 Monitoring & Alerts

- **CloudWatch Dashboard** tracks:
  - CPU utilization
  - Memory usage
  - Request metrics
- **CloudWatch Alarm** triggers when:
  - ECS CPU usage exceeds **70% for 5 minutes**
- **SNS Topic** sends alert notifications:
  - Delivered via **email** when thresholds are breached

---

## 🔐 Security Measures

- **IAM Roles**:
  - Configured with **least-privilege** permissions for ECS tasks
- **Secrets Management**:
  - Secrets injected securely using **AWS Secrets Manager**
- **Security Groups**:
  - Ingress only on required ports: **80, 443, 8000**
- **SSL Termination**:
  - **ALB** currently serves traffic over HTTP. HTTPS and SSL termination can be configured using **AWS ACM**.

---

## ⚖️ Load Balancing Test

- **ALB Routing**:
  - Routes `*/api/*` traffic to the **backend service**
  - Routes all other traffic to the **frontend**
- **High Availability**:
  - Minimum **2 tasks** running per service for redundancy
- **Zero-Downtime Failover**:
  - Backend continues functioning if one task fails or is stopped

## 🎥 Demo Video

📽️ [Click here to watch the full walkthrough](#)  
<!-- Replace `#` with your actual video link -->

---

## 🤝 Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 🧾 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## ✨ Author

**Joel Chandanshiv**

- 🚀 [LinkedIn](https://www.linkedin.com/in/joel-chandanshiv/)  
- 📫 Reach me via [GitHub](https://github.com/JoelChandanshiv) or email: `joelchandanshiv@gmail.com`

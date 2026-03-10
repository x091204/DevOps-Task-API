# DevOps-Task-API

use the mainv1 branch

A simple To-Do web application built with **Flask**, HTML, and CSS.

This project is a **practice application for learning DevOps tools** and demonstrates a full CI/CD pipeline.

## 🛠️ DevOps Tools Used

| Tool | Purpose | Status |
|------|---------|--------|
| Jenkins | CI/CD Pipeline | ✅ Done |
| Docker | Containerization | ✅ Done |
| Docker Hub | Image Registry | ✅ Done |
| Trivy | Security Scanning | 🔄 In Progress |
| Kubernetes | Container Orchestration | 🔄 In Progress |
| Terraform | Infrastructure as Code | 🔄 In Progress |

---

## 🔁 CI/CD Pipeline Flow
```
Code Push → Clone → Build → Test → Docker Build → Push to DockerHub → Deploy
```

---

## ✨ App Features

- Add tasks
- Mark tasks as completed
- Delete tasks
- Clean modern UI with dark theme

---

## 📁 Project Structure
```
DevOps-Task-API/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── Jenkinsfile
├── conftest.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── tests/
    └── test_app.py
```

---

## © Copyright
© 2026 xwazo — Built as part of my DevOps learning journey.

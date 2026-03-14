# DevOps-Task-API 🚀

A simple To-Do web application built with **Flask**, HTML, and CSS — used as a hands-on project to learn and implement real-world DevOps tools and practices.

> Instead of just watching tutorials, I built something real and applied every DevOps tool I learn directly to a working project.

---

## 🛠️ Tech Stack

| Tool | Purpose | Status |
|------|---------|--------|
| Python / Flask | Web application | ✅ Done |
| Jenkins | CI/CD Pipeline | ✅ Done |
| Docker | Containerization | ✅ Done |
| Docker Hub | Image Registry | ✅ Done |
| Trivy | Security Scanning + SBOM | ✅ Done |
| Docker Compose | Multi-container setup | ⏳ In Progress |
| Kubernetes | Container Orchestration | ⏳ In Progress |
| Terraform | Infrastructure as Code | ⏳ In Progress |
| Prometheus | Metrics & Monitoring | ⏳ In Progress |
| Grafana | Monitoring Dashboards | ⏳ In Progress |
| AWS | Cloud Deployment | ⏳ In Progress |

---

## 🏗️ CI/CD Pipeline Flow

```
Code Push → Clone → Build → Test → Docker Build → Trivy Scan → Push to DockerHub → Deploy
```

### Pipeline Stages
| Stage | Description |
|-------|-------------|
| Clone | Pull latest code from GitHub |
| Build | Create venv + install dependencies |
| Test | Run pytest test suite |
| Docker Build | Build image tagged with BUILD_NUMBER |
| Trivy Scan | Scan for HIGH/CRITICAL vulnerabilities + generate SBOM |
| Push | Push verified image to Docker Hub |
| Deploy | Stop old container, run new one |

---

## 🔐 Security

- Trivy scans every image before it reaches Docker Hub
- HTML vulnerability report archived as Jenkins artifact
- SBOM generated in CycloneDX format every build
- Pipeline fails automatically if HIGH/CRITICAL vulnerabilities found
- Credentials managed securely via Jenkins credentials store

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
├── app.py                  ← Flask application
├── requirements.txt        ← Production dependencies
├── requirements-dev.txt    ← Dev/test dependencies
├── Dockerfile              ← Container definition
├── .dockerignore           ← Files excluded from Docker image
├── .gitignore              ← Files excluded from Git
├── .trivyignore            ← Accepted/false positive CVEs
├── Jenkinsfile             ← CI/CD pipeline definition
├── conftest.py             ← pytest path configuration
├── templates/
│   └── index.html          ← Frontend HTML
├── static/
│   └── style.css           ← Styling
└── tests/
    └── test_app.py         ← Application tests
```

---

## 🚀 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/x091204/DevOps-Task-API.git
cd DevOps-Task-API

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements-dev.txt

# Run the app
python app.py
```

App runs at: `http://localhost:5000`

---

## 🔮 Roadmap

- [x] Jenkins CI/CD pipeline
- [x] Docker containerization
- [x] Docker Hub image registry
- [x] Trivy security scanning + SBOM
- [ ] Docker Compose multi-container setup
- [ ] Kubernetes deployment
- [ ] Terraform infrastructure provisioning
- [ ] AWS deployment with Load Balancer + Auto Scaling
- [ ] Prometheus + Grafana monitoring

---

## 📅 Timeline

| Phase | Tasks | Status |
|-------|-------|--------|
| Phase 1 | Jenkins + Docker + DockerHub | ✅ Done |
| Phase 2 | Trivy Security Scanning | ✅ Done |
| Phase 3 | Docker Compose | ⏳ In Progress |
| Phase 4 | Kubernetes | ⏳ In Progress |
| Phase 5 | Terraform | ⏳ In Progress |
| Phase 6 | AWS + Load Balancer + Auto Scaling | ⏳ In Progress |
| Phase 7 | Prometheus + Grafana | ⏳ In Progress |

---

## © Copyright
© 2026 xwazo — Built as part of my DevOps learning journey.

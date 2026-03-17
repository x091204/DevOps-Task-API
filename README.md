# DevOps-Task-API 🚀

A two-tier To-Do web application built with **Flask** and **MySQL** — used as a hands-on project to learn and implement real-world DevOps tools and practices.

> Instead of just watching tutorials, I built something real and applied every DevOps tool I learn directly to a working project.

---

## 🛠️ Tech Stack

| Tool | Purpose | Status |
|------|---------|--------|
| Jenkins | CI/CD Pipeline | ✅ Done |
| Docker | Containerization | ✅ Done |
| Docker Hub | Image Registry | ✅ Done |
| Trivy | Security Scanning + SBOM | ✅ Done |
| Docker Compose | Multi-container setup | ✅ Done |

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
| Test | Run pytest test suite with mocked DB |
| Docker Build | Build image tagged with BUILD_NUMBER |
| Trivy Scan | Scan for HIGH/CRITICAL vulnerabilities + generate SBOM |
| Push | Push verified image to Docker Hub |
| Deploy | Docker Compose brings up Flask + MySQL |

---

## 🏛️ Architecture

```
                    Jenkins CI/CD
                         ↓
GitHub Push → Build → Test → Trivy Scan → DockerHub
                                               ↓
                                    Docker Compose Deploy
                                         ↓         ↓
                                    Flask App    MySQL DB
                                    (port 5000)  (persistent volume)
```

---

## 🔐 Security

- Trivy scans every image before it reaches Docker Hub
- HTML vulnerability report archived as Jenkins artifact
- SBOM generated in CycloneDX format every build
- Pipeline fails automatically if HIGH/CRITICAL vulnerabilities found
- Credentials managed securely — never hardcoded
- `.env` file never committed to Git

---

## ✨ App Features

- Add tasks
- Mark tasks as completed
- Delete tasks
- Data persists across restarts (MySQL backend)
- Clean modern UI with dark theme
- Health check endpoint (`/health`)

---

## 📁 Project Structure

```
DevOps-Task-API/
├── app.py                  ← Flask application + MySQL connection
├── requirements.txt        ← Production dependencies
├── requirements-dev.txt    ← Dev/test dependencies
├── Dockerfile              ← Container definition
├── docker-compose.yml      ← Multi-container setup (Flask + MySQL)
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
    └── test_app.py         ← Application tests (mocked DB)
```

---

## 🚀 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/x091204/DevOps-Task-API.git
cd DevOps-Task-API

# Create .env file with your credentials
# MYSQL_ROOT_PASSWORD=yourpassword
# MYSQL_DATABASE=tasksdb
# MYSQL_USER=root
# MYSQL_PASSWORD=yourpassword

# Run with Docker Compose
docker-compose up -d
```

App runs at: `http://localhost:5000`

---

## 🔮 Roadmap

- [x] Jenkins CI/CD pipeline
- [x] Docker containerization
- [x] Docker Hub image registry
- [x] Trivy security scanning + SBOM
- [x] Docker Compose multi-container setup
- [x] MySQL persistent database
- [x] Automated testing with mocked DB
- [x] Health check endpoint

---

## © Copyright
© 2026 xwazo — Built as part of my DevOps learning journey.

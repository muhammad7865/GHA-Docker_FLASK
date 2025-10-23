# GHA-Docker_FLASK

A collaborative Flask web application with automated CI/CD pipeline and Docker containerization.

---

## 📋 Team Roles & Responsibilities

### **Member 1 - Backend Developer** (`member1_backend/`)

**Role:** Backend development and API implementation

- Develops and maintains Flask application routes and endpoints
- Implements business logic and data processing
- Creates and manages backend services
- Writes unit tests for backend functionality
- Handles database integration (if applicable)

### **Member 2 - Frontend Developer** (`member2_frontend/`)

**Role:** Frontend/UI development and client-side integration

- Designs and implements user interfaces
- Creates HTML templates and static assets (CSS, JavaScript)
- Develops client-side form validation and interactions
- Integrates frontend with backend API endpoints
- Ensures responsive design and user experience

### **Member 3 - DevOps Engineer** (`member3_devops/`)

**Role:** CI/CD pipeline, containerization, and deployment

- Sets up and maintains GitHub Actions workflows
- Configures Docker containerization
- Manages deployment pipelines
- Monitors application performance
- Handles infrastructure and automation tasks

---

## 🏗️ Project Structure

```
GHA-Docker_FLASK/
│
├── main/                       # Main application directory
│   ├── app.py                  # Flask application entry point
│   ├── requirements.txt        # Python dependencies
│   ├── Dockerfile             # Docker configuration
│   ├── templates/             # HTML templates
│   │   └── index.html         # Main page template
│   ├── static/                # Static assets (CSS, JS)
│   │   └── styles.css         # Application styles
│   └── tests/                 # Unit tests
│       └── test_app.py        # Application tests
│
├── member1_backend/           # Backend work directory
├── member2_frontend/          # Frontend work directory
├── member3_devops/            # DevOps work directory
│
└── .github/
    └── workflows/
        ├── ci-cd.yml          # CI/CD testing pipeline
        └── docker.yml         # Docker build & push pipeline
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** installed
- **Docker** (optional, for containerization)
- **Git** for version control
- **Docker Hub account** (for pushing images)

---

## 💻 Local Development

### 1. Clone the Repository

```powershell
git clone https://github.com/muhammad7865/GHA-Docker_FLASK.git
cd GHA-Docker_FLASK
```

### 2. Set Up Virtual Environment (Recommended)

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux/Mac:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```powershell
pip install --upgrade pip
pip install -r main/requirements.txt
```

### 4. Run the Application

```powershell
cd main
python app.py
```

The application will be available at: **http://localhost:5000**

### 5. Run Tests

From the repository root:

```powershell
pytest main/tests/test_app.py -v
```

Expected output:

```
tests/test_app.py::test_home PASSED       [33%]
tests/test_app.py::test_health PASSED     [66%]
tests/test_app.py::test_data_post PASSED  [100%]
```

---

## 🐳 Docker Setup

### Build Docker Image

```powershell
docker build -t gha-docker-flask:latest -f main/Dockerfile main/
```

### Run Docker Container

```powershell
docker run -p 5000:5000 gha-docker-flask:latest
```

Access the application at: **http://localhost:5000**

### Stop Container

```powershell
docker ps                          # Find container ID
docker stop <container-id>
```

---

## 🔄 CI/CD Pipeline

### GitHub Actions Workflows

#### **1. CI/CD Testing Pipeline** (`ci-cd.yml`)

- **Triggers:** Push or Pull Request to `main` branch
- **Steps:**
  1. Checkout repository
  2. Set up Python 3.8
  3. Install dependencies from `main/requirements.txt`
  4. Run pytest on `main/tests/test_app.py`

#### **2. Docker Build & Push Pipeline** (`docker.yml`)

- **Triggers:** Push or Pull Request to `main` branch
- **Steps:**
  1. Checkout repository
  2. Log in to Docker Hub
  3. Build Docker image from `main/Dockerfile`
  4. Push image to Docker Hub as `<username>/gha-docker-flask:latest`

### Required GitHub Secrets

To enable Docker push, add these secrets in GitHub repository settings:

| Secret Name       | Description              | Example             |
| ----------------- | ------------------------ | ------------------- |
| `DOCKER_USERNAME` | Your Docker Hub username | `muhammad7865`      |
| `DOCKER_TOKEN`    | Docker Hub access token  | `dckr_pat_xxxxx...` |

**How to add secrets:**

1. Go to: `Settings` → `Secrets and variables` → `Actions`
2. Click `New repository secret`
3. Add both `DOCKER_USERNAME` and `DOCKER_TOKEN`

---

## 🧪 API Endpoints

### **GET /**

Returns the main HTML page with a form.

**Response:** HTML page

---

### **GET /health**

Health check endpoint.

**Response:**

```json
{
  "status": "OK"
}
```

---

### **POST /data**

Accepts JSON data and returns a confirmation message.

**Request Body:**

```json
{
  "name": "Your Name"
}
```

**Success Response (201):**

```json
{
  "message": "Data received successfully!",
  "data": {
    "name": "Your Name"
  }
}
```

**Error Response (400):**

```json
{
  "error": "No JSON data provided"
}
```

---

## 🔧 Development Workflow

### Branching Strategy

- `main` - Production-ready code
- `member1_backend` - Backend development
- `member2_frontend` - Frontend development
- `member3_devops` - DevOps and CI/CD work

### Making Changes

1. **Create/Switch to your branch:**

   ```powershell
   git checkout -b member1_backend
   ```

2. **Make your changes** in your designated directory

3. **Test locally:**

   ```powershell
   pytest main/tests/test_app.py
   ```

4. **Commit and push:**

   ```powershell
   git add .
   git commit -m "Descriptive message"
   git push origin member1_backend
   ```

5. **Create Pull Request** to `main` branch on GitHub

---

## 📦 Dependencies

### Python Packages (`requirements.txt`)

- **Flask 3.0.2** - Web framework
- **pytest 8.3.3** - Testing framework

---

## 🐛 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'flask'`

**Solution:** Install dependencies

```powershell
pip install -r main/requirements.txt
```

### Issue: Tests not found

**Solution:** Run pytest from repository root

```powershell
pytest main/tests/test_app.py
```

### Issue: Docker build fails

**Solution:** Ensure you're building from correct context

```powershell
docker build -t gha-docker-flask -f main/Dockerfile main/
```

### Issue: Port 5000 already in use

**Solution:** Kill existing process or use different port

```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill process (replace PID)
taskkill /PID <PID> /F

# Or run on different port
python app.py  # Edit app.py to change port
```

---

## 📝 License

This project is created for educational purposes.

---

## 👥 Contributors

- **Member 1** - Backend Development
- **Member 2** - Frontend Development
- **Member 3** - DevOps & CI/CD

---

## 📞 Support

For issues or questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Review GitHub Actions logs for CI/CD errors
3. Create an issue in the repository

---

**Happy Coding! 🚀**

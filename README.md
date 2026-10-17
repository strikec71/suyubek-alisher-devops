# Suyubek Alisher DevOps Laboratory

**Suyubek Alisher · IT2-2306 · Student ID 37773 · DevOps**

Personal laboratory project: Linux → Git → GitHub → Docker → Jenkins.

Repository: https://github.com/strikec71/suyubek-alisher-devops

## Requirements

Ubuntu 24.04 ARM64 or AMD64, Git, Python 3.12, Docker Engine and the Compose plugin.
Automation requires Jenkins LTS, Java 21, and the Pipeline and Git plugins.
The application uses only the Python standard library.

## Prepare a fresh clone

```bash
mkdir -p ~/devops
git clone https://github.com/strikec71/suyubek-alisher-devops.git ~/devops/suyubek_alisher
cd ~/devops/suyubek_alisher
./scripts/prepare_demo.sh
cp .env.example .env
```

The ignored logs/application.log and backup/ directory are generated locally.
.gitignore rules do not stop tracking files that were committed earlier.

## Checks

```bash
./scripts/Suyubek_Alisher_system.sh
python3 -m compileall -q app tests
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

## Docker

```bash
docker build -t suyubek-alisher-devops .
docker run -d --name suyubek-alisher-container \
  -p 127.0.0.1:8000:8000 \
  -e STUDENT_NAME=Alisher -e STUDENT_SURNAME=Suyubek \
  -e STUDENT_GROUP=IT2-2306 -e STUDENT_ID=37773 \
  suyubek-alisher-devops
curl -fsS http://127.0.0.1:8000/student
docker logs suyubek-alisher-container
docker stop suyubek-alisher-container
docker rm suyubek-alisher-container
```

## Compose

Stop and remove the manually started container first:

```bash
cp .env.example .env
docker compose up -d --build
docker compose ps
docker compose logs --tail=20
docker compose down
```

Compose, manual execution and Jenkins use the same container name and port 8000;
run them one at a time. EXPOSE documents the port; -p publishes it.

## Application and environment variables

/ is the student page; /student returns JSON; /health checks readiness.
STUDENT_NAME, STUDENT_SURNAME, STUDENT_GROUP and STUDENT_ID are read at startup.
The defaults identify Suyubek Alisher. APP_PORT overrides the port in
config/app.conf; APP_CONFIG can select a different configuration file.
Inside the container, the server listens on 0.0.0.0. Startup information and
request logs are available through docker logs.

## Jenkins

Create a Pipeline job named **Suyubek_Alisher_DevOps**. Select Pipeline script from
SCM, this repository's Git URL, branch */main and Script Path Jenkinsfile.
The Linux node requires Python, Git, Docker CLI and Docker daemon access for jenkins.

Checkout → Build → Test → Docker Build → Docker Run.
Build checks Python compilation. Test executes real unit and HTTP tests.
Docker Run waits for /health, verifies every /student field and leaves the container
running. Stage errors are not suppressed. Repeated builds execute sequentially.
The commit SHA is printed in the console and stored in an OCI image label.

## Demonstration files

private.txt contains harmless demonstration text only. Permissions 600 and 644 are
applied in Linux by prepare_demo.sh; Git preserves the executable bit, not every
chmod permission. config/app.conf contains the application port actually used by
the server. Passwords, tokens, .env, backups and logs must stay outside Git and images.

## Readiness verification

```bash
curl -fsS http://127.0.0.1:8000/health
python3 -m scripts.check_running
```

The first command returns OK. The second waits for readiness and compares all four
/student fields against the expected environment variables. A mismatch returns
an error status.

## Demonstration and recovery

- docs/COMMANDS.md: commands and explanations for the individual verification.
- docs/VIDEO_SCRIPT.md: a continuous demonstration with the student's own voice.
- infra/README.md: Ubuntu installation and Jenkins recovery.
- infra/plugins.lock.txt: the plugin versions verified on the current environment.

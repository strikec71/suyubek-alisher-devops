# Demonstration and individual verification commands

Suyubek Alisher · IT2-2306 · Student ID 37773

Run these commands inside Ubuntu from ~/devops/suyubek_alisher. Docker, Compose
and Jenkins share one application container, so demonstrate them sequentially.

## Linux

```bash
pwd
ls -la
cd app
pwd
cd ..
mkdir -p backup
./scripts/prepare_demo.sh
touch backup/demo.txt
cp Suyubek_Alisher_info.txt backup/info_copy.txt
mv backup/info_copy.txt backup/info_saved.txt
cat backup/info_saved.txt
head -n 3 backup/info_saved.txt
tail -n 2 backup/info_saved.txt
rm backup/demo.txt backup/info_saved.txt
find . -type f -name application.log
grep ERROR logs/application.log
grep WARNING logs/application.log
grep -c ERROR logs/application.log
tail -n 5 logs/application.log
chmod 600 private.txt
chmod 644 public.txt
ls -l private.txt public.txt
./scripts/Suyubek_Alisher_system.sh
ps
ps aux
top
```

pwd prints the current directory; ls lists its contents; cd changes directory;
mkdir creates a directory; touch creates a file or updates its timestamp;
cp copies; mv moves or renames; rm removes; cat prints file contents;
head and tail display the beginning and end.

600 = rw-------; 644 = rw-r--r--; 755 = rwxr-xr-x.
Owner, group and others have independent permission sets: r=4, w=2, x=1.
ps provides a snapshot; top updates process information continuously (press q to
exit). PID is the process identifier.

## Git

```bash
git config --show-origin --get user.name
git config --show-origin --get user.email
git status
git log --oneline
git branch
git log --oneline --graph --all
git remote -v
git check-ignore -v logs/application.log backup/demo.txt .env
git ls-files '*.log' 'backup/*' '.env'
```

Git tracks versions; GitHub hosts the remote repository. A branch separates
changes, and merge combines them. push sends commits; pull retrieves and
integrates changes. .gitignore prevents adding local files. To stop tracking
an already committed file, use git rm --cached.

## Docker

```bash
docker images suyubek-alisher-devops
docker ps
docker ps -a
docker logs suyubek-alisher-container
docker exec suyubek-alisher-container python --version
docker stop suyubek-alisher-container
docker start suyubek-alisher-container
curl -fsS http://127.0.0.1:8000/student
docker stop suyubek-alisher-container
docker rm suyubek-alisher-container
cp .env.example .env
docker compose up -d --build
docker compose ps
docker compose logs --tail=20
docker compose down
```

An image packages the application and its environment; a container is a running
instance. FROM selects the base; WORKDIR sets the directory for later instructions;
COPY adds files; RUN executes during the build; CMD runs when a container starts;
EXPOSE documents a port. Environment variables change configuration without a
rebuild. Do not embed secrets in the image. Compose describes execution in YAML
and makes it repeatable with one command.

After Compose, run Jenkins Build Now to leave the application running again.

## Jenkins and the integrated workflow

Open Suyubek_Alisher_DevOps. Show its SCM URL, main branch, Jenkinsfile, five stages,
build number, commit SHA, student information and Finished: SUCCESS.

Checkout retrieves source code. Build checks syntax. Test checks behavior.
Docker Build creates the image. Docker Run starts and verifies the container.
A nonzero stage exit status fails the build; subsequent ordinary stages are
normally skipped. Do not replace real checks with echo or suppress failures
using || true.

Complete workflow: edit → test → commit → push → Build Now →
Checkout/Build/Test/Docker Build/Docker Run → SUCCESS → updated application.

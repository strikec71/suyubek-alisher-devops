# Recovering the laboratory Jenkins environment

Suyubek Alisher · IT2-2306 · Student ID 37773

On a fresh Ubuntu 24.04 machine, run from the project root:

```bash
sudo bash scripts/install_ubuntu.sh
```

The script installs Java 21, Jenkins LTS, Docker Engine and Compose from their
official repositories. It is intended for a dedicated Linux laboratory environment.
After installation, start a new user session, check docker version and verify
access for the Jenkins service:

```bash
sudo -u jenkins -H docker version
```

Unlock Jenkins, create your administrator account and install Pipeline, Git and
Pipeline Stage View. plugins.lock.txt records the versions verified on the current
installation. The official Jenkins Plugin Installation Manager can install this
list using the file and the matching Jenkins WAR.

jenkins-job.xml exports the job definition without passwords or tokens. Import it
using Jenkins CLI create-job, or configure the job manually as explained in README.
Jenkinsfile stays in GitHub: Definition Pipeline script from SCM, SCM Git,
branch */main. Do not commit Jenkins credentials or private SSH keys.

The current Mac environment uses Lima 2.2.1 and Ubuntu 24.04.5 LTS ARM64, with
4 virtual CPUs, 8 GiB RAM and a 60 GiB disk. Lima uses macOS Virtualization.framework.
The Linux project is stored in ~/devops/suyubek_alisher. The docker and jenkins
services are enabled at Ubuntu startup.

The Locale plugin sets English as the Jenkins interface language for consistent
English demonstration screenshots. The recorded plugin lock includes this plugin.

After installing Locale, run infra/set_english_locale.groovy in the authenticated
Jenkins Script Console to apply the English interface settings.

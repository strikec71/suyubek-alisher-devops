# Восстановление учебного Jenkins

Suyubek Alisher · IT2-2306 · 37773

На чистой Ubuntu 24.04 выполнить из корня проекта:

```bash
sudo bash scripts/install_ubuntu.sh
```

Скрипт устанавливает Java 21, Jenkins LTS, Docker Engine и Compose из официальных
репозиториев. Он предназначен для отдельного учебного Linux стенда. После установки
перевойти в сеанс пользователя, проверить `docker version` и доступ службы:

```bash
sudo -u jenkins -H docker version
```

Разблокировать Jenkins, создать личного администратора, установить Pipeline, Git и
Pipeline Stage View. В plugins.lock.txt зафиксированы фактически проверенные версии
всех плагинов текущего стенда. Для установки такого набора можно использовать
официальный Jenkins Plugin Installation Manager с этим файлом и текущим Jenkins WAR.

jenkins-job.xml — экспорт определения Job без паролей и токенов. Импортировать его
через Jenkins CLI create-job либо создать Job вручную по README. Jenkinsfile
остаётся в GitHub: Definition Pipeline script from SCM, SCM Git, ветка */main.
Личные Jenkins credentials и SSH private key в репозиторий не включаются.

Фактический стенд на Mac использует Lima 2.2.1 и Ubuntu 24.04.5 LTS ARM64,
4 виртуальных CPU, 8 GiB RAM, диск 60 GiB. Lima использует macOS Virtualization.framework.
Файлы Linux проекта находятся в ~/devops/suyubek_alisher внутри VM;
службы docker и jenkins включены в автозапуск Ubuntu.

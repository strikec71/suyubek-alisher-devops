# Команды для демонстрации и защиты

Suyubek Alisher · IT2-2306 · 37773

Выполнять в Ubuntu из `~/devops/suyubek_alisher`. Это учебная последовательность;
Docker, Compose и Jenkins используют один контейнер, поэтому запускаются по очереди.

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

`pwd` — текущий каталог; `ls` — содержимое; `cd` — переход; `mkdir` — создание каталога;
`touch` — создание файла/обновление времени; `cp` — копирование; `mv` — перемещение;
`rm` — удаление; `cat` — содержимое; `head/tail` — начало/конец.
`600` = rw-------; `644` = rw-r--r--; `755` = rwxr-xr-x.
Владелец, группа и остальные получают независимые наборы r=4, w=2, x=1.
`ps` показывает снимок, `top` обновляет данные (выход q). PID — идентификатор процесса.

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

Git хранит версии, GitHub предоставляет удалённый репозиторий.
Ветка отделяет изменения, merge объединяет их. push отправляет коммиты,
pull получает и интегрирует изменения. .gitignore защищает от добавления
локальных файлов; уже отслеживаемый файл требует `git rm --cached`.

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

Образ — шаблон приложения и среды; контейнер — запущенный экземпляр.
FROM задаёт базу, WORKDIR каталог для следующих инструкций, COPY добавляет файлы,
RUN выполняется при сборке, CMD при старте контейнера, EXPOSE документирует порт.
Env меняет конфигурацию без пересборки; секреты не помещаются в образ.
Compose описывает запуск в YAML и позволяет повторить его одной командой.

После Compose запустить Jenkins Build Now, чтобы снова оставить приложение работающим.

## Jenkins и интеграция

Открыть Job Suyubek_Alisher_DevOps. Показать SCM URL, main, Jenkinsfile,
пять стадий, номер сборки, commit SHA, личные данные и Finished: SUCCESS.

Checkout получает исходники. Build проверяет синтаксис. Test проверяет поведение.
Docker Build создаёт образ. Docker Run запускает и проверяет контейнер.
При ненулевом коде стадии сборка падает, следующие стадии обычно пропускаются.
Нельзя заменять реальные проверки выводом echo или скрывать ошибки через `|| true`.

Полный цикл: изменить приложение → проверить → commit → push → Build Now →
Checkout/Build/Test/Docker Build/Docker Run → SUCCESS → обновлённая страница.

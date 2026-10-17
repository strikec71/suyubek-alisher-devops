# Suyubek Alisher DevOps Laboratory

**Suyubek Alisher · IT2-2306 · Student ID 37773 · DevOps**

Персональный проект лабораторной: Linux → Git → GitHub → Docker → Jenkins.

Репозиторий: https://github.com/strikec71/suyubek-alisher-devops

## Требования

Ubuntu 24.04 ARM64 или AMD64, Git, Python 3.12, Docker Engine с Compose plugin.
Для автоматизации: Jenkins LTS, Java 21, плагины Pipeline и Git.
Приложение использует только стандартную библиотеку Python.

## Подготовка после clone

```bash
git clone https://github.com/strikec71/suyubek-alisher-devops.git
cd suyubek-alisher-devops
./scripts/prepare_demo.sh
cp .env.example .env
```

Игнорируемые logs/application.log и backup/ создаются локально.
Правила .gitignore не отменяют отслеживание ранее добавленных файлов.

## Проверки

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

После остановки и удаления ручного контейнера:

```bash
cp .env.example .env
docker compose up -d --build
docker compose ps
docker compose logs --tail=20
docker compose down
```

Compose, ручной запуск и Jenkins используют одно имя контейнера и порт 8000;
запускать их последовательно. EXPOSE документирует порт, а -p публикует его.

## Приложение и переменные

/ — персональная страница; /student — JSON; /health — проверка готовности.
STUDENT_NAME, STUDENT_SURNAME, STUDENT_GROUP, STUDENT_ID читаются при запуске.
По умолчанию используются данные Suyubek Alisher. APP_PORT переопределяет порт
из config/app.conf; APP_CONFIG может указать другой конфигурационный файл.
Внутри контейнера сервер слушает 0.0.0.0. Данные выводятся также в docker logs.

## Jenkins

Создать Pipeline Job **Suyubek_Alisher_DevOps**, выбрать Pipeline script from SCM,
Git URL этого репозитория, ветку */main, Script Path Jenkinsfile.
На Linux узле нужны Python, Git, Docker CLI и доступ пользователя jenkins к daemon.

Checkout → Build → Test → Docker Build → Docker Run.
Build проверяет компиляцию Python. Test запускает реальные unit/HTTP тесты.
Docker Run ожидает /health, сверяет все поля /student и оставляет контейнер запущенным.
Ошибки стадий не скрываются. Повторные сборки выполняются последовательно.
Commit SHA выводится в журнал и сохраняется в OCI label образа.

## Учебные файлы

private.txt содержит только демонстрационный текст. Права 600 и 644 показываются
в Linux после prepare_demo.sh; Git сохраняет executable bit, а не полный chmod.
В config/app.conf хранится используемый приложением порт. Пароли, токены, .env,
резервные копии и журналы не должны попадать в Git или Docker image.

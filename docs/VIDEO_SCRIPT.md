# Personal video demonstration script

Record one continuous video with your own voice. The assignment recommends
10-20 minutes. This script supports the explanation; it is not evidence that
the video has already been recorded.

## 0-1 minute Introduction

“My name is Suyubek Alisher, group IT2-2306, Student ID 37773. I will demonstrate
my project, Linux commands, GitHub repository, Docker and Jenkins Pipeline.”
Show Suyubek_Alisher_info.txt and the project directory structure.

## 1-5 minutes Linux

Follow docs/COMMANDS.md. Show pwd, ls, cd, mkdir, touch, cp, mv, rm, cat, head and
tail using temporary copies. Find application.log, display ERROR and WARNING
messages, count the two ERROR messages and show the last five lines.
Explain permissions 600/644 and owner/group/others. Run the system script and
explain its file-existence check. Show ps, ps aux and top; identify PID, owner,
CPU and memory usage. Avoid reading entire system tables aloud.

## 5-8 minutes Git and GitHub

Show git status, identity, meaningful commits, development and merge.
Show git check-ignore and the empty git ls-files result for ignored paths.
Open your public GitHub repository. Explain local versus remote repositories,
push versus pull and the purpose of branches.

## 8-12 minutes Docker

Explain the six required Dockerfile instructions. Show the image and container,
docker logs, STUDENT_NAME/SURNAME/GROUP/ID, /student and stop/start/exec/rm.
Then demonstrate Compose up/ps/logs/down. Remove the manual container first to
release its name and port. Use the README commands as needed.

## 12-18 minutes Jenkins and the complete workflow

Open Suyubek_Alisher_DevOps and show the GitHub URL, main and Jenkinsfile.
Make one small real change, run tests, commit and push from Ubuntu.
Click Build Now. Explain Checkout, Build, Test, Docker Build and Docker Run.
Show the student fields, commit SHA, ten tests and Finished: SUCCESS in Console
Output. Show the running container and the application's updated message.

## 18-19 minutes Explanation and submission

Explain Linux → Git → GitHub → Jenkins → Docker. A failed stage must fail the
Pipeline; subsequent ordinary stages are skipped. Show the repository link
and the prepared PDF report.

## Before recording

On Mac, press Shift+Command+5, select screen recording and choose the microphone
under Options. Make a short test recording and listen to it. Increase terminal
font size. Do not show Jenkins_access_PRIVATE.txt, private SSH keys or passwords.
The assignment requires your own voice; it does not require a webcam image.

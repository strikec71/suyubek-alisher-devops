#!/usr/bin/env bash
set -eu
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
printf '%s\n' '==============================' 'Student Information' '=============================='
printf '%s\n' 'Name: Alisher' 'Surname: Suyubek' 'Group: IT2-2306' 'Student ID: 37773'
printf '%s\n' '==============================' 'System Information' '=============================='
printf 'Username: '; whoami
printf 'Hostname: '; hostname
printf 'Current Date: '; date -Iseconds
printf 'Operating System: '; uname -a
printf '\nDisk Usage:\n'; df -h
printf '\nMemory Usage:\n'; free -h
if [ -f "$ROOT/Suyubek_Alisher_info.txt" ]; then
  printf '\nStudent information file exists.\n'
else
  printf '\nStudent information file does not exist.\n'
fi

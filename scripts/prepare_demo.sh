#!/usr/bin/env bash
set -eu
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
mkdir -p "$ROOT/logs" "$ROOT/backup"
cat > "$ROOT/logs/application.log" <<'LOG'
INFO Application started
INFO User logged in
WARNING Configuration file missing
INFO Database connected
ERROR Database connection failed
INFO Application restarted
WARNING Memory usage is high
INFO Request received
ERROR Request failed
INFO Application stopped
LOG
chmod 600 "$ROOT/private.txt"
chmod 644 "$ROOT/public.txt"
printf 'Prepared logs, backup, and permissions in %s\n' "$ROOT"

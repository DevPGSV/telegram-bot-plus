#!/usr/bin/env bash

THIS_DIR=$(cd $(dirname $0); pwd)
cd ~/telegram-bot-plus/

socat -h >/dev/null 2>&1 || ( echo >&2 "socat is not installed. Plase install and try again."; exit 1; )

rm -f /tmp/tgbp.sck
(sleep 2;echo "quit" | socat - UNIX-CONNECT:/tmp/tgbp.sck >/dev/null 2>&1)&
./tg/bin/telegram-cli -E -k ./tg/tg-server.pub -e quit -Z ./bot/launcher.py -C -D -R -S /tmp/tgbp.sck && (ex_status=0;) || ( ex_status=1;echo "ERROR!"; exit 1;)

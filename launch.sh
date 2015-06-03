#!/usr/bin/env bash
cd $(cd $(dirname $0); pwd)

if [ ! -f ./tg/telegram.h ]; then
  echo "tg not found"
  echo "Run $0 install"
  exit 1
fi

if [ ! -f ./tg/bin/telegram-cli ]; then
  echo "tg binary not found"
  echo "Run $0 install"
  exit 1
fi

./tg/bin/telegram-cli -k ./tg/tg-server.pub -Z ./bot/launcher.py -W -l 0 $@

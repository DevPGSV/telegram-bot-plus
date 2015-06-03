#!/usr/bin/env bash

THIS_DIR=$(cd $(dirname $0); pwd)
cd $THIS_DIR
RAM=`grep MemTotal /proc/meminfo | awk '{print $2}'`

install() {
  chmod +x launch.sh
  git pull
  git submodule update --init --recursive
  cd tg && ./configure && make
  RET=$?;
  if [ $RET -ne 0 ]; then
    echo "Error. Exiting."
    exit $RET
  fi
  cd ..
}

update() {
  git pull
  git submodule update --init --recursive
}

if [ "$1" = "update" ]; then
  update
else
  if [ -f ./tg/bin/telegram-cli ]; then
    echo "You already have telegram-cli"
    echo "Use $0 to update"
    exit 1
  else
    install
  fi
fi
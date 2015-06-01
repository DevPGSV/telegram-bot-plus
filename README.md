telegram-bot-plus
=================

Installation
------------

Debian:

```bash
sudo apt-get install libreadline-dev libconfig-dev libssl-dev libevent-dev libjansson-dev python-dev make unzip git python-pip
cd $HOME
git clone https://github.com/DevPGSV/telegram-bot-plus.git
cd telegram-bot-plus
./setup.sh
./launch.sh # Will ask you for a phone number & confirmation code.
```

For a better experience, start the bot with this command:

```bash
./launch.sh -D -R
```
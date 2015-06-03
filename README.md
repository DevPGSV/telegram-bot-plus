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

If you want to call tg-cli with parameters, add them after ./launch. If you have profiles:

```bash
./launch.sh -p profileName
```


[Emoji cheatsheet](http://www.emoji-cheat-sheet.com/)

Open port in terminal:

```bash
nc -v localhost 8080
main_session
```

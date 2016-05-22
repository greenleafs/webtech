#!/bin/bash
# git clone https://github.com/greenleafs/webtech.git web
# cd web
cp ask/ask/default_settings.py ask/ask/settings.py
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/test-nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo service mysql start
mysql -uroot -e "create database wtech"
cd ask
./manage.py syncdb --noinput
gunicorn -b 0.0.0.0:8000 ask.wsgi
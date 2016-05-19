#!/bin/bash
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/test-nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

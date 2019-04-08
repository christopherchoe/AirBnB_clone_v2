#!/usr/bin/env bash
# sets up server nginx and directories
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
echo "simple content" | sudo tee -a /data/web_static/releases/test/index.html
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/relases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/^}/i location /web_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-enabled/default
sudo service nginx restart

#!/bin/bash
# Init
FILE="/tmp/out.$$"
GREP="/bin/grep"

# Make sure only root can run our script
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# Preparing System
apt-get install git python3-pip -y


#Preparing python libraries
pip3 install requests

#apt-get install python3-sqlalchemy
pip3 install SQLAlchemy

pip3 install Flask
pip3 install multiprocessing
pip3 install PyYaml
pip3 install PyGithub
pip3 install icalendar
pip3 install feedparser
#Extra script needed for async version
pip3 install aiohttp

#Get the code
git clone https://github.com/ninjatrench/DeveloperHorizon

cd DeveloperHorizon
echo "Follow following commands"
echo ""
echo "Enter the directory"
echo ">> cd DeveloperHorizon"
echo ""
echo "Adjust the configurations at config/config.cfg including host, port and github access token etc.."
echo ">> nano config/config.cfg"
echo ""
echo "Replace http://localhost:5000/ with http://<IP>:<PORT>/ as mentioned in config file in static"
echo ">> nano static/js/dashboard.min.js"
echo ""
echo "Set default_config_file location in controler/config.py"
echo ">> nano controller/conf.py"
echo ""
echo "finally run flask main app"
echo ">> python3 main.py"

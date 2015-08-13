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
apt-get install git
apt-get install python3-pip


#Preparing python libraries
pip3 install requests

#apt-get install python3-sqlalchemy
pip3 install SQLAlchemy

pip3 install Flask
pip3 install multiprocessing
pip3 install PyYaml
pip3 install PyGithub
pip3 install icalendar

#Extra script needed for async version
pip3 install aiohttp

#Get the code
git clone https://github.com/ninjatrench/DeveloperHorizon

cd DeveloperHorizon
echo "Adjust the config files at config/config.cfg"
echo "Replace http://localhost:5000/ with http://<IP>:<PORT>/ as mentioned in config file"
echo "Set default_config_file in conf.py"
echo "Run python3 main.py"
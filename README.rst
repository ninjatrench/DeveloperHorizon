.. image:: https://img.shields.io/badge/build-passing-green.svg
    :target: https://github.com/ninjatrench/DeveloperHorizon

.. image:: https://img.shields.io/badge/version-stable-green.svg
    :target: https://github.com/ninjatrench/DeveloperHorizon

.. image:: https://img.shields.io/badge/with%20love%20from-india-ff69b4.svg
    :alt: Make In India <3


Documentation and Wiki
-------------
DeveloperHorizon is a dashboard which is used for managing github issues, Debian Package issues, Debian Conference calender, Ubuntu loco events, Bitcuket issues tracking, bugzilla tracking, remote iCalendar files and
combine everything into single iCalendar, RSS, or JSON file

This project is part of Google Summer of Code 2015 under Debian community.

Full documentation is available at https://wiki.debian.org/SummerOfCode2015/DeveloperDashboard

Project Mentors
-------------
- Daniel Pocock (https://github.com/irl)
- Iain R. Learmonth (https://github.com/dpocock)

How to install and use
-------------
I have recently written a one step installation script for this project
just fetch the setup.sh script and run/pipe it to bash

.. code-block:: pycon

    curl https://raw.githubusercontent.com/ninjatrench/DeveloperHorizon/master/setup.sh | bash
    
    
or

.. code-block:: pycon

    wget https://raw.githubusercontent.com/ninjatrench/DeveloperHorizon/master/setup.sh -o setup.sh
    chmod +x setup.sh
    bash setup.sh
    
it will automatically install all the required dependency, fetch the code and prepare the environment for it.
currently it is written for using with Debian and Ubuntu, but it can be altered easily to work with other linux distributions.

help is welcome for writing the script for that.

Technologies and reference
-------------
I have implemented rest API architecture for the project
so backend and front end works separately

So you can run web API and User interface separately
or skip the UI all together and just use the web API
or build your own UI over the webAPI

Reference usage of REST web API is at : https://github.com/ninjatrench/DeveloperHorizon/blob/master/examples/Flask_api_usage.txt

Backend:
- Python3
- Flash microframework for handling url and web api
- SQLalchemy and JSON for storage
- python-multiprocessing for concurrent processing

Front end is written in
- HTML5
- CSS 3
- Angular JS
- Twitter bootstrap
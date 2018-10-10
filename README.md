# LumoCash Sentinel

An all-powerful toolset for LumoCash.

Sentinel is an autonomous agent for persisting, processing and automating LumoCash 1.0.x governance objects and tasks.

Sentinel is implemented as a Python application that binds to a local version 1.0.x lumocashd instance on each LumoCash 1.0.x Masternode.

This guide covers installing Sentinel onto an existing 1.0.x Masternode in Ubuntu 16.04.

## Installation

### 1. Install Prerequisites

Make sure Python version 2.7.x or above is installed:

    python --version

Update system packages and ensure virtualenv is installed:

    $ sudo apt-get update
    $ sudo apt-get -y install python-virtualenv

Make sure the local LumoCash daemon running is at least version 1.0.x 

    $ lumocash-cli getinfo | grep version

### 2. Install Sentinel

Clone the Sentinel repo and install Python dependencies.

    $ git clone https://github.com/LumoCash2018/Sentinel.git sentinel && cd sentinel
    $ virtualenv ./venv
    $ ./venv/bin/pip install -r requirements.txt

### 3. Set up Cron

Set up a crontab entry to call Sentinel every minute:

    $ crontab -e

In the crontab editor, add the lines below, replacing '/home/YOURUSERNAME/sentinel' to the path where you cloned sentinel to:

    * * * * * cd /home/YOURUSERNAME/sentinel && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1

## Configuration

An alternative (non-default) path to the `lumocash.conf` file can be specified in `sentinel.conf`:

    lumocash_conf=/path/to/lumocash.conf

## Troubleshooting

To view debug output, set the `SENTINEL_DEBUG` environment variable to anything non-zero, then run the script manually:

    $ SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py

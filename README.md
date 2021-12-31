# Dynamic DNS for Gandi.net LiveDns

A small application that discovers the local IP addresses
and forwards the information to Gandi.net's LiveDns service.

## Configuring the service

You'll need an API Key from Gandi.net:
  * Login to Gandi.net
  * Account > Security > Generate API Key
  * Insert the api key into `config.py`

You need to setup the service with systemd / etc.
  * Edit dyndns.service with the user & directory you want to run it as.
  * Copy `systemd/*` into `/etc/systemd/system`



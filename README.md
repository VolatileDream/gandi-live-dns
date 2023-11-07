# Dynamic DNS for Gandi.net LiveDns

A small application that discovers the local IP addresses
and forwards the information to Gandi.net's LiveDns service.

## Configuring the service

You'll need an API Key from Gandi.net:
  * Login to Gandi.net
  * User Settings > Personal Access Token > Create token
  * Select the organization that contains your domains.
  * Restrict to selected products: select only the domain you want to be updating.
  * Add permission "Manage domain name technical configurations"
  * Create!
  * Insert the api key into `config.py` under `access_token`

You need to setup the service with systemd / etc.
  * Edit dyndns.service with the user & directory you want to run it as.
  * Copy `systemd/*` into `/etc/systemd/system`



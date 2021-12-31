#!/usr/bin/python3

import config
import json
import requests
import subprocess

gandi_api = 'https://api.gandi.net'


def headers():
  h = {
    'Connection': None,
    'Content-Type': 'application/json',
    'Authorization': 'Apikey ' + config.api_key
  }
  return h


def update_registration(ip4=None, ip6=None):
  payload = []
  if ip4:
    payload.append({
      'rrset_name': config.subdomain,
      'rrset_type': "A",
      'rrset_ttl': 300,
      'rrset_values': [ip4],
    })
  if ip6:
    payload.append({
      'rrset_name': config.subdomain,
      'rrset_type': "AAAA",
      'rrset_ttl': 300,
      'rrset_values': [ip6],
    })

  u = gandi_api + '/v5/livedns/domains/%s/records/%s' % (config.domain, config.subdomain)
  response = requests.put(u, json={'items':payload}, headers=headers())
  if response.status_code != 200 and response.status_code != 201:
    print('Error updating ip for record: %s\n%s' % (u, response._content))
    return False

  return json.loads(response._content)


def icanhazip(ip4):
  flag = "-4"
  if not ip4:
    flag = "-6"

  # This is terrible, but will work.
  proc = subprocess.run(["curl", flag, "http://icanhazip.com"], capture_output=True)
  if proc.returncode == 0:
    return str(proc.stdout.strip(), "utf8")

  return None


def validate_config():
  errors = []
  if not config.api_key:
    errors.append("No api key provided")
  if not config.domain:
    errors.append("No domain configured")
  if not config.subdomain:
    errors.append("No subdomain specified")

  if errors:
    raise Exception(errors)


def m():
  validate_config()
  ip4, ip6 = (icanhazip(True), icanhazip(False))
  update_registration(ip4=ip4, ip6=ip6)


if __name__ == "__main__": m()

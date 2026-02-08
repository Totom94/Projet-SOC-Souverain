#!/usr/bin/env python3

import sys
import requests
import json

alert_file = sys.argv[1]
hook_url = sys.argv[3]

with open(alert_file) as f:
    alert_json = json.load(f)

try:
    response = requests.post(hook_url, json=alert_json, headers={"Content-Type": "application/json"}, timeout=10)
    if response.status_code != 200:
        print(f"Erreur lors de l'envoi à n8n : {response.status_code} {response.text}")
except Exception as e:
    print(f"Exception lors de l'envoi à n8n : {e}")

sys.exit(0)

#!/bin/bash
# Sends a GET request to URL then display response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"

#!/bin/bash
# Send a GET request to URL with header variable.
curl -sH "X-School-User-Id: 98" "${1}"

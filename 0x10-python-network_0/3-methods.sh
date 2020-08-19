#!/bin/bash
# Displays all HTTP methods the server will accept.
curl -sI "$1" | awk '/Allow/' | cut -b 8-

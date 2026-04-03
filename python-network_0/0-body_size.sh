#!/bin/bash
# Displays the size of the body of the response for a given URL
curl -s "$1" | wc -c

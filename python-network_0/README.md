# Python - Network #0

This project involves using Bash scripts with `curl` to interact with HTTP servers and process responses. Each script is designed to perform a specific networking task and adheres to strict formatting requirements.

## Learning Objectives

At the end of this project, you should be able to explain:
- What a URL is
- What HTTP is
- The anatomy of an HTTP request and response
- HTTP headers and methods (GET, POST, DELETE, etc.)
- How to use `curl` for basic networking tasks
- HTTP cookies and their purpose

## Requirements

### Bash Scripts
- Interpreted on Ubuntu 20.04 LTS
- Exactly 3 lines long
- All files end with a new line
- All files are executable
- The first line is `#!/bin/bash`
- The second line is a comment describing the script
- All `curl` commands use the `-s` (silent) option

## Tasks

0. **cURL body size**: Displays the size of the response body in bytes.
1. **cURL to the end**: Displays the body of a 200 status code response.
2. **cURL Method**: Sends a DELETE request and displays the body.
3. **cURL only methods**: Displays all HTTP methods accepted by the server.
4. **cURL headers**: Sends a GET request with a custom header and displays the body.
5. **cURL POST parameters**: Sends a POST request with parameters and displays the body.

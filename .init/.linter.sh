#!/bin/bash
cd /home/kavia/workspace/code-generation/timeserverapi-1982-eaee5d65/time_api_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi


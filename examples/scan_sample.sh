#!/usr/bin/env bash
set -euo pipefail

# The scanner analyzes source text; it never executes this sample file.
mcp-audit "$(dirname "$0")/suspicious_server.py"

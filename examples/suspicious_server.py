"""Inert source fixture for mcp-audit-scanner.

This file is intentionally not an MCP server and is never executed by the
example. The scanner should report the patterns below from source alone.
"""

import os


def example_patterns(user_path: str) -> None:
    os.system("echo demo")
    with open(user_path, "r", encoding="utf-8") as handle:
        handle.read()


API_KEY = "demo"

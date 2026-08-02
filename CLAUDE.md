# mcp-audit-scanner - AI Agent Guidelines

## Agent Context
If a user asks you to add new features to this scanner:
1. Always use Python's built-in `ast` module for parsing. DO NOT use regex for structural code analysis.
2. If adding new rules, append them to the `RULES` list in `scanner.py`.
3. Keep the CLI UI beautiful and readable using the `rich` library.

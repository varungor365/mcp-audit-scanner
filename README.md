# MCP Audit Scanner

**Static analysis CLI for auditing Model Context Protocol (MCP) servers before you connect them to an AI client.**

[![PyPI version](https://badge.fury.io/py/mcp-audit-scanner.svg)](https://badge.fury.io/py/mcp-audit-scanner)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## ✨ Why this exists

Developers are connecting third-party Model Context Protocol (MCP) servers to local IDEs and AI agents. A static preflight review can catch risky filesystem, subprocess, and credential patterns before a server is trusted.

**mcp-audit-scanner** statically analyzes Python-based MCP servers using AST (Abstract Syntax Tree) to detect insecure patterns like direct `os.system()` calls, unrestricted `open()`, and hardcoded secrets.

### Features

- **Static AST analysis:** Parses Python source without executing it.
- **High-signal rules:** Flags shell/subprocess calls, unrestricted `open()`, and API-key-like assignments.
- **Readable output:** Uses `rich` to display rule IDs, severity, locations, and snippets.
- **Local-first operation:** Performs no network access and does not modify the scanned code.

## Limitations

This is a small Python AST preflight, not a complete security assessment. It does not execute code, resolve imports, inspect non-Python MCP servers, prove that a server is safe, or replace dependency scanning, sandboxing, least-privilege review, or human approval. A clean result means only that the current rules did not match the scanned source.

---

## 🚀 Quickstart

The repository includes [examples/scan_sample.sh](examples/scan_sample.sh), which scans an intentionally suspicious but never executed Python file. The scanner parses source code with AST and does not run the sample.

### Install
```bash
pip install mcp-audit-scanner
```

### Usage

Scan an entire MCP server directory:
```bash
mcp-audit ./my-mcp-server/
```

Scan a single file:
```bash
mcp-audit server.py
```

---

## 🤖 AI Agent Context

See [CLAUDE.md](CLAUDE.md) for contribution guidelines.

---

## 📄 License

MIT © Varun Ruhella. See [LICENSE](LICENSE) for details.

## Who this is for

Use MCP Audit Scanner when you need a repeatable static review of Model Context Protocol server definitions, tool exposure, configuration risk, or security hygiene before connecting an MCP server to an AI client.

## Why star this repository

Star this project if you are building MCP tooling, evaluating AI-agent integrations, or want a small security-focused CLI to extend with your own audit rules.

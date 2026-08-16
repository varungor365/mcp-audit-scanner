<div align="center">

# 🛡️ mcp-audit-scanner

**Static analysis CLI tool for auditing Model Context Protocol (MCP) servers.**

[![PyPI version](https://badge.fury.io/py/mcp-audit-scanner.svg)](https://badge.fury.io/py/mcp-audit-scanner)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<br/>

</div>

---

## ✨ Why this exists

With the rise of the Model Context Protocol (MCP), developers are plugging third-party servers into their local IDEs and AI agents. If these MCP servers have unrestricted file system access or vulnerable prompt injections, your machine is at risk.

**mcp-audit-scanner** statically analyzes Python-based MCP servers using AST (Abstract Syntax Tree) to detect insecure patterns like direct `os.system()` calls, unrestricted `open()`, and hardcoded secrets.

### Features
- 🔍 **Static AST Analysis:** Parses your Python code without executing it.
- 🚫 **Catches Common Vulns:** Flags `os.system`, `subprocess.run`, unrestricted `open()`.
- 🎨 **Beautiful Output:** Uses `rich` to display vulnerabilities in an easy-to-read table.

---

## 🚀 Quickstart

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

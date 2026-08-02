import ast
import os
from typing import List, Dict

class Rule:
    def __init__(self, id: str, description: str, severity: str):
        self.id = id
        self.description = description
        self.severity = severity

RULES = [
    Rule("MCP001", "Unrestricted filesystem access (e.g. open(), os.system() without path validation)", "HIGH"),
    Rule("MCP002", "Potential prompt injection in subprocess or shell calls", "CRITICAL"),
    Rule("MCP003", "Hardcoded API keys or secrets", "HIGH")
]

def scan_file(filepath: str) -> List[Dict]:
    results = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            tree = ast.parse(content)
            
            for node in ast.walk(tree):
                # MCP001 & MCP002: Check for subprocess/os.system/open
                if isinstance(node, ast.Call):
                    if isinstance(node.func, ast.Attribute):
                        if node.func.attr in ['system', 'popen', 'run'] and getattr(node.func.value, 'id', '') in ['os', 'subprocess']:
                            results.append({
                                "rule": RULES[1],
                                "line": node.lineno,
                                "file": filepath,
                                "snippet": ast.unparse(node)
                            })
                    elif isinstance(node.func, ast.Name):
                        if node.func.id == 'open':
                            results.append({
                                "rule": RULES[0],
                                "line": node.lineno,
                                "file": filepath,
                                "snippet": ast.unparse(node)
                            })
                            
                # MCP003: Check for hardcoded API keys
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name) and 'API_KEY' in target.id.upper():
                            if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                                results.append({
                                    "rule": RULES[2],
                                    "line": node.lineno,
                                    "file": filepath,
                                    "snippet": ast.unparse(node)
                                })
    except Exception as e:
        # Ignore parse errors for non-python files or invalid syntax
        pass
        
    return results

def scan_directory(dirpath: str) -> List[Dict]:
    all_results = []
    for root, _, files in os.walk(dirpath):
        for file in files:
            if file.endswith('.py'):
                all_results.extend(scan_file(os.path.join(root, file)))
    return all_results

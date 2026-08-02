import pytest
import os
import tempfile
from mcp_auditor.scanner import scan_file

def test_scan_subprocess():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write("import os\n")
        f.write("def my_func():\n")
        f.write("    os.system('rm -rf /')\n")
        filepath = f.name
        
    try:
        results = scan_file(filepath)
        assert len(results) == 1
        assert results[0]["rule"].id == "MCP002"
        assert "os.system" in results[0]["snippet"]
    finally:
        os.remove(filepath)

def test_scan_open():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write("def read_file(path):\n")
        f.write("    return open(path, 'r').read()\n")
        filepath = f.name
        
    try:
        results = scan_file(filepath)
        assert len(results) == 1
        assert results[0]["rule"].id == "MCP001"
        assert "open" in results[0]["snippet"]
    finally:
        os.remove(filepath)

def test_scan_hardcoded_key():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write("MY_API_KEY = 'sk-12345'\n")
        filepath = f.name
        
    try:
        results = scan_file(filepath)
        assert len(results) == 1
        assert results[0]["rule"].id == "MCP003"
    finally:
        os.remove(filepath)

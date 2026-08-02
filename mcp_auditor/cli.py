import argparse
import os
import sys

from rich.console import Console
from rich.table import Table

from mcp_auditor.scanner import scan_directory, scan_file

console = Console()

def main():
    parser = argparse.ArgumentParser(description="🛡️ MCP Audit Scanner")
    parser.add_argument("path", help="Directory or file to scan")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.path):
        console.print(f"[bold red]Path not found:[/bold red] {args.path}")
        sys.exit(1)
        
    console.print(f"[bold cyan]Scanning MCP Server at:[/bold cyan] {args.path}")
    
    if os.path.isdir(args.path):
        results = scan_directory(args.path)
    else:
        results = scan_file(args.path)
        
    if not results:
        console.print("\n[bold green]✅ No vulnerabilities found! Your MCP server looks secure.[/bold green]")
        return
        
    table = Table(title="🛡️ Vulnerabilities Detected")
    table.add_column("Rule ID", style="cyan")
    table.add_column("Severity", style="red")
    table.add_column("File:Line", style="magenta")
    table.add_column("Description")
    table.add_column("Code Snippet", style="yellow")
    
    for res in results:
        severity_color = "red" if res["rule"].severity == "CRITICAL" else "yellow"
        table.add_row(
            res["rule"].id,
            f"[{severity_color}]{res['rule'].severity}[/{severity_color}]",
            f"{os.path.basename(res['file'])}:{res['line']}",
            res["rule"].description,
            res["snippet"]
        )
        
    console.print("\n")
    console.print(table)
    sys.exit(1)

if __name__ == "__main__":
    main()

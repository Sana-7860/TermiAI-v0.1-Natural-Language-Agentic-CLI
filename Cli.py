# CLI/UX - Rich Terminal UI and Approval Prompts
# Owner: Sana-7860 - Workstream 6

from rich.console import Console
from rich.prompt import Confirm

console = Console()

def display_response(text: str):
    console.print(f"[bold green]TermiAI:[/] {text}")

def approval_prompt(action: str) -> bool:
    return Confirm.ask(f"[yellow]Allow action: {action}?[/]")

def show_banner():
    console.print("[bold blue]TermiAI v0.1 - Natural Language CLI[/]")

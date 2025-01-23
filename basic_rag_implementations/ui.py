import subprocess
from rich.console import Console
from rich.panel import Panel
import time

console = Console()

console.print(Panel("Welcome! Type 'help' for more info, or 'init' to start", title="RAG Terminal"))

while True:
    # Get user input
    user_input = console.input("[bold green]>>> [/bold green]")

    # Exit condition
    if user_input.lower() == "exit":
        try:
            result = subprocess.run(
                ["python", "populate_database.py", "--reset"],
                capture_output=False,
                text=True
            )
            console.print("Remember to close your server!")
        except:
            console.print("There was an issue clearing the Chroma Database")

        console.print("[bold red]Exiting...[/bold red]")
        break

    elif user_input.lower() == "init":
        try:
            # Open a new PowerShell window and run Ollama serve
            console.print("[bold green]> [/bold green]", end='')
            console.print("Starting Ollama Server... ", end='')
            subprocess.Popen(
                ["start", "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe", "-NoExit", "-Command", "ollama serve"],
                shell=True
            )
            time.sleep(5)
            console.print("Done")
            

            console.print("[bold green]> [/bold green]", end='')
            console.print("Starting Vector Database... ")
            result = subprocess.run(
                ["python", "populate_database.py"],
                capture_output=False,
                text=True
            )
            console.print("[bold green]> [/bold green]", end='')
            console.print("Done")

        except Exception as e:
            console.print(f"[bold red]There was an issue: {e}[/bold red]")

    elif user_input.lower() == 'help':
        console.print("Here are a list of commands:")
        console.print("[bold]init:[/bold] Starts the server and populates your database")
        console.print("[bold]exit:[/bold] Stops all processes and exits - however does not kill the server")
        console.print("[bold]ask:[/bold] everything after this keyword will be sent to the RAG system")

    elif user_input.lower().startswith("ask"):
        # Extract arguments (everything after 'ask')
        parts = user_input.split(maxsplit=1)
        if len(parts) < 2:
            console.print("[bold yellow]Usage: ask \"<query>\"[/bold yellow]")
            continue
        arguments = parts[1].strip('"')  # Remove surrounding quotes if present

        # console.print(f"[bold blue]Executing: python query_data.py \"{arguments}\"[/bold blue]")
        console.print("[bold green]> [/bold green]", end='')
        console.print("[bold white]Processing...")
        try:
            # Run the command with arguments
            result = subprocess.run(
                ["python", "query_data.py", arguments],
                capture_output=True,
                text=True
            )
            # Print the output
            console.print(Panel(f"[bold green]Output[/bold green]\n{result.stdout}"))
            #console.print(result.stdout)

            if result.stderr:
                console.print("[bold red]Error:[/bold red]")
                console.print(result.stderr)

        except FileNotFoundError:
            console.print("[bold red]Error: python or query_data.py not found![/bold red]")


    else:
        console.print(f"[yellow]Unknown command: {user_input}[/yellow]")

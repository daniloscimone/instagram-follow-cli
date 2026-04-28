"""Command-line interface for instagram-follow-cli."""

from __future__ import annotations

import argparse
from typing import Sequence

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text

from .compare import find_non_reciprocal_following
from .instagram_export import load_export_data


console = Console()


def show_banner() -> None:
    """Render a compact welcome banner in the terminal."""

    title = Text("Instagram Follow CLI", style="bold cyan")
    subtitle = Text(
        "Confronta follower e following usando solo API ufficiali, senza scraping.",
        style="white",
    )
    console.print(
        Panel(
            subtitle,
            title=title,
            border_style="bright_magenta",
            padding=(1, 2),
        )
    )


def show_info(message: str, *, title: str = "Info", style: str = "cyan") -> None:
    """Show an informational panel."""

    console.print(Panel(message, title=title, border_style=style, padding=(1, 2)))


def show_error(message: str, *, title: str = "Errore") -> None:
    """Show an error panel."""

    console.print(Panel(message, title=title, border_style="red", padding=(1, 2)))


def show_success(message: str, *, title: str = "Completato") -> None:
    """Show a success panel."""

    console.print(Panel(message, title=title, border_style="green", padding=(1, 2)))


def show_non_reciprocal_table(username: str, accounts: Sequence[str]) -> None:
    """Render the non-reciprocal accounts as a table."""

    table = Table(title=f"Account seguiti da @{username} che non seguono indietro")
    table.add_column("#", style="dim", justify="right", width=4)
    table.add_column("Username", style="bright_cyan")

    for index, account in enumerate(accounts, start=1):
        table.add_row(str(index), account)

    console.print(table)


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser."""

    parser = argparse.ArgumentParser(
        prog="instagram-follow-cli",
        description="Confronta follower e following di Instagram usando le API ufficiali.",
    )
    parser.add_argument(
        "--username",
        help="Username Instagram da analizzare. Se omesso, viene richiesto in modo interattivo.",
    )
    parser.add_argument(
        "--export",
        help="Percorso all'export ufficiale Instagram (.zip, cartella estratta o .json).",
    )
    return parser


def prompt_username() -> str:
    """Ask the user for the Instagram username."""

    username = Prompt.ask("Inserisci lo username Instagram").strip()
    if not username:
        raise ValueError("Lo username non può essere vuoto.")
    return username


def run(
    username: str,
    *,
    followers: Sequence[str] | None = None,
    following: Sequence[str] | None = None,
) -> int:
    """Run the comparison workflow for a single username."""

    show_info(
        f"Analisi avviata per @{username}.\n\n"
        "La CLI userà le API ufficiali e segnalerà chiaramente se serve un login autorizzato.",
        title="Avvio",
        style="bright_blue",
    )

    assert followers is not None
    assert following is not None

    non_reciprocal = find_non_reciprocal_following(followers, following)

    if not non_reciprocal:
        show_success(f"Nessun account non ricambiato trovato per @{username}.")
        return 0

    show_non_reciprocal_table(username, non_reciprocal)
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point for the console script."""

    show_banner()
    parser = build_parser()
    args = parser.parse_args(argv)
    username = args.username or prompt_username()
    export_path = args.export or Prompt.ask(
        "Percorso all'export ufficiale Instagram (.zip, cartella estratta o .json)",
    )

    show_info(
        "Per gli account privati questo strumento non usa API personali o scraping.\n"
        "Scarica il tuo export ufficiale Instagram dopo il login e poi confronta follower e following in locale.",
        title="Flusso ufficiale",
        style="bright_blue",
    )

    data = load_export_data(export_path)
    show_info(
        f"Dati caricati correttamente: {len(data.followers)} follower e {len(data.following)} following.",
        title="Import riuscito",
        style="green",
    )

    return run(username, followers=data.followers, following=data.following)


if __name__ == "__main__":
    raise SystemExit(main())

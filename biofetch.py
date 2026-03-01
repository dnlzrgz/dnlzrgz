# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "rich>=14.3.3",
# ]
# ///

from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console(record=True, width=80)


ascii_art = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡠⠖⢉⣌⢆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠚⠉⠀⠈⠉⠲⣿⣿⡜⡀⠀⠀⠀⠀
⡔⢉⣙⣓⣒⡲⠮⡇⠀⠀⠀⠀⠀⠀⠘⡿⡇⡇⠀⠀⠀⠀
⡇⠘⣿⣿⣿⠏⠀⠀⠠⣀⡀⠀⠀⠀⠀⡇⠈⠳⡄⠀⠀⠀
⢹⠀⢻⣿⠇⠀⠀⣀⣀⠀⡍⠃⠀⠀⣠⣷⡟⢳⡜⡄⠀⠀
⠈⣆⠀⠋⢀⢔⣵⣿⠋⠹⣿⠒⠒⠚⠁⣿⣿⣾⣷⢸⠤⡄
⠀⡇⠀⠀⢸⢸⣿⣿⣶⣾⡏⡇⠀⠀⢀⡘⣝⠿⡻⢸⡰⠁
⠀⢳⠀⠀⠈⢆⠻⢿⡿⠟⡱⠁⠰⠛⢿⡇⠀⠉⠀⡸⠁⠀
⠀⠈⢆⠀⠀⠀⠉⠒⠒⣉⡀⠀⠀⢇⠀⡇⠀⠀⢠⠃⠀⠀
⠀⠀⠈⠣⡀⠀⠀⠀⠀⠀⢉⡱⠀⠀⠉⠀⢀⡴⠁⠀⠀⠀
⠀⠀⠀⠀⠈⠓⠦⣀⣉⡉⠁⢀⣀⣠⠤⠒⠥⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⣉⣀⣀⡠⠭⠛⠀⠀⠑⠒⠤⠤⠷⠀⠀⠀
"""


def create_table(
    title: str,
    subtitle: str,
    rows: list[tuple[str, str]],
) -> Table:
    table = Table.grid(padding=(0, 1))
    table.add_row(f"[bold]{title}[/]", f"{subtitle}")

    for i, (label, value) in enumerate(rows):
        is_last = i == len(rows) - 1
        prefix = "└" if is_last else "├"
        table.add_row(f"{prefix}[bold]{label}[/]", value)

    return table


def main() -> None:
    right_column = Group(
        create_table(
            "User",
            "",
            [
                ("WEB", "dnlzrgz.com"),
                ("MAIL", "contact@dnlzrgz.com"),
                ("GIT", "github.com/dnlzrgz"),
                ("IN", "linkedin.com/in/dnlzrgz"),
                ("LANG", "es, en, fr, it"),
                ("LOC", "Spain, Alicante"),
            ],
        ),
        Text(" "),
        create_table(
            "Stack",
            "",
            [
                ("BACK", "Django, DRF, FastAPI"),
                ("FRONT", "React, Next.js, TailwindCSS"),
                ("DB", "PostgreSQL, SQLite, Redis"),
                ("OPS", "Docker, Git, Linux"),
                ("OTHER", "Go, Rust, C, Java"),
            ],
        ),
        Text(" "),
        Panel(
            Text("I'm participating in the Djangonaut Program!"),
            title="[bold]News![/]",
            title_align="left",
        ),
    )

    layout = Table.grid(padding=3)
    layout.add_row(
        Text(ascii_art, overflow="ignore"),
        right_column,
    )
    console.print(
        Panel(
            layout,
            title="[bold]biofetch.py[/]",
            title_align="left",
            border_style="bright_black",
            padding=(1, 2),
            expand=True,
        ),
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(
            f"<div align='center'><pre>\n{console.export_text(clear=False)}\n</pre></div>"
        )


if __name__ == "__main__":
    main()

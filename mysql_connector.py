import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from rich.console import Console
from rich.table import Table
from rich import box

connection_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="",
    host="localhost",
    port=3306,
    database="hos",
)

engine = create_engine(connection_url)
console = Console()

try:
    df = pd.read_sql("SELECT * FROM ovst", engine)

    columns_to_show = [
        "hn",
        "vstdate",
        "vsttime",
        "name"
    ]
    existing_cols = [c for c in columns_to_show if c in df.columns]
    filtered_df = df[existing_cols]

    table = Table(
        box=box.SQUARE,
        show_lines=True,
        header_style="white",
        title_style="bold yellow",
    )

    for col in existing_cols:
        table.add_column(col, overflow="fold")

    for row in filtered_df.itertuples(index=False):
        table.add_row(*[str(v) for v in row])

    console.print(table)

except Exception as e:
    console.print(f"[red]เกิดข้อผิดพลาด:[/red] {e}")

finally:
    engine.dispose()

import os

from invoke import task


@task
def run(c, filename):
    path = os.path.abspath(os.path.dirname(__file__))
    # Windows環境用のコマンド
    if os.name == "nt":
        c.run(f"set PYTHONPATH=%PYTHONPATH%;{path} & python {filename}")
    else:
        c.run(f'export PYTHONPATH="$PYTHONPATH:{path}" && python {filename}')


@task
def split(c, filename):
    path = os.path.abspath(os.path.dirname(__file__))
    from src.util import generate_path

    if os.name == "nt":
        c.run(f"python ./src/split.py")
    else:
        c.run(f'export PYTHONPATH="$PYTHONPATH:{path}" && python /src/split.py')

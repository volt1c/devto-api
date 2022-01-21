import subprocess


def start_dev():
    subprocess.run('poetry run uvicorn devtoapi:app --reload'.split())


def start():
    subprocess.run('poetry run uvicorn devtoapi:app'.split())

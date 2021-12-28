"""RP Todo entry point script"""
# todo_cli/__main__.py

from todo_cli import cli, __app_name__

def main():
    cli.app(prog_name=__app_name__)

if __name__ == '__main__':
    main()
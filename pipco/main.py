import argparse
import subprocess
import os

# 定义可用的pip源
PIP_SOURCES = {
    "pypi": "https://pypi.python.org/simple/",
    "douban": "https://pypi.douban.com/simple/",
    "aliyun": "https://mirrors.aliyun.com/pypi/simple/",
    "qinghua": "https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/"
}


def show_help():
    help_message = """
    pco - A simple tool to manage pip sources.

    Usage:
    pco help           Show this help message
    pco now            Show the current pip source
    pco use SOURCE     Switch to the specified pip source
    pco ls             List available pip sources

    Available sources:
    pypi, douban, aliyun, qinghua
    """
    print(help_message)


def show_current_source():
    if os.name == 'nt':  # Windows
        pip_config_file = os.path.join(os.path.expanduser('~'), 'pip', 'pip.ini')
    else:  # macOS and Linux
        pip_config_file = os.path.join(os.path.expanduser('~'), '.pip', 'pip.conf')
        print(pip_config_file)

    try:
        with open(pip_config_file, 'r') as file:
            config = file.read()
            for source in PIP_SOURCES.values():
                if source in config:
                    print(f"Current pip source: {source}")
                    return
        print("No custom pip source found, using default.")
    except FileNotFoundError:
        print("No custom pip source configuration file found, using default.")


def switch_source(source_name):
    if source_name not in PIP_SOURCES:
        print(f"Unknown source: {source_name}")
        return

    source_url = PIP_SOURCES[source_name]

    if os.name == 'nt':  # Windows
        pip_config_file = os.path.join(os.path.expanduser('~'), 'pip', 'pip.ini')
        config_content = f"[global]\nindex-url = {source_url}"
    else:  # macOS and Linux
        pip_config_file = os.path.join(os.path.expanduser('~'), '.pip', 'pip.conf')
        config_content = f"[global]\nindex-url = {source_url}"

    os.makedirs(os.path.dirname(pip_config_file), exist_ok=True)
    with open(pip_config_file, 'w') as file:
        file.write(config_content)

    print(f"Switched to {source_name} source: {source_url}")


def list_sources():
    print("Available pip sources:")
    for name, url in PIP_SOURCES.items():
        print(f"{name}: {url}")


def main():
    parser = argparse.ArgumentParser(description="Manage pip sources.")
    parser.add_argument('command', choices=['help', 'now', 'use', 'ls'], help="Command to execute")
    parser.add_argument('source', nargs='?', help="Source to switch to (for 'use' command)")

    args = parser.parse_args()

    if args.command == 'help':
        show_help()
    elif args.command == 'now':
        show_current_source()
    elif args.command == 'use':
        if not args.source:
            print("Please specify a source to switch to.")
        else:
            switch_source(args.source)
    elif args.command == 'ls':
        list_sources()
    else:
        print("Unknown command. Use 'pco help' for usage information.")


if __name__ == "__main__":
    main()
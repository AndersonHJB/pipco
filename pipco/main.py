import argparse
import subprocess

# 定义可用的pip源
SOURCES = {
    "pypi": "https://pypi.python.org/simple/",
    "douban": "http://pypi.douban.com/simple/",
    "aliyun": "http://mirrors.aliyun.com/pypi/simple/",
    "qinghua": "https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/"
}


def list_sources():
    for name, url in SOURCES.items():
        print(f"{name}: {url}")


def get_current_source():
    result = subprocess.run(['pip', 'config', 'get', 'global.index-url'], capture_output=True, text=True)
    if result.stdout:
        print("当前pip源:", result.stdout.strip())
    else:
        print("未设置pip源")


def set_source(name):
    if name in SOURCES:
        subprocess.run(['pip', 'config', 'set', 'global.index-url', SOURCES[name]])
        print(f"已切换到源: {name}")
    else:
        print("未找到指定的源，请使用pco ls查看所有可用的源")


def main():
    parser = argparse.ArgumentParser(description='管理pip源的工具')
    parser.add_argument('command', help='命令（now, use, ls）')
    parser.add_argument('source', nargs='?', help='源名称')

    args = parser.parse_args()

    if args.command == 'ls':
        list_sources()
    elif args.command == 'now':
        get_current_source()
    elif args.command == 'user' and args.source:
        set_source(args.source)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

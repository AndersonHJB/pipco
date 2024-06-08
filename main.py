import argparse
import configparser
import sys

# 配置源的字典
SOURCES = {
    "pypi": "https://pypi.python.org/simple/",
    "douban": "http://pypi.douban.com/simple/",
    "aliyun": "http://mirrors.aliyun.com/pypi/simple/",
    "qinghua": "https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/"
}


def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


def save_config(config):
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def show_current_source():
    config = load_config()
    print("当前pip源是：", config['default']['source'])


def change_source(source_name):
    config = load_terms()
    if source_name in SOURCES:
        config['default'] = {'source': SOURCES[source_name]}
        save_config(config)
        print(f"已切换到 {source_name} 源")
    else:
        print("未找到指定的源，请检查源名称是否正确。")


def list_sources():
    for name, url in SOURCES.items():
        print(f"{name}: {url}")


def main():
    parser = argparse.ArgumentParser(description='PIPCO - Python Change Source Tool')
    parser.add_argument('command', choices=['now', 'use', 'ls'], help='Command to execute')
    parser.add_argument('source', nargs='?', help='Source name to switch to')
    args = parser.parse_args()

    if args.command == 'now':
        show_current_source()
    elif args.command == 'use':
        change_source(args.source)
    elif args.command == 'ls':
        list_sources()


if __name__ == "__main__":
    main()

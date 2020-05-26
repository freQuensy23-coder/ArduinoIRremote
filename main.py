import json


def read_from_json(filename):
    with open(filename) as f:
        result = json.load(f)
        return result


def main():
    keys = read_from_json("config.json")


if __name__ == '__main__':
    main()
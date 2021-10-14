import argparse
from collections import Counter


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fin")
    return parser.parse_args()


def main(args):
    words = Counter()
    for fname in args.fin.strip().split(","):
        with open(fname) as fin:
            for line in fin:
                words.update(line.strip().split())
    print(len(words))


if __name__ == "__main__":
    main(parse_args())

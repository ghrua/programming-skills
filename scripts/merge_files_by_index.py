import argparse
from os.path import exists
import subprocess as sp
import json


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prefix", type=str)
    parser.add_argument("--type", choices=['json', 'txt'],
                        type=str, default='txt')
    parser.add_argument("--output", type=str, default="output.txt")
    parser.add_argument("--start_index", type=int, default=0)
    parser.add_argument("--end_index", type=int)
    return parser.parse_args()


def merge_text(args):
    for idx in range(args.start_index, args.end_index+1):
        fname = "{}.{}".format(args.prefix, idx)
        if exists(fname):
            sp.run("cat {} >> {}".format(fname, args.output), shell=True)
        else:
            print("[Warning] cannot find file: {}".format(fname))


def merge_json(args):
    buf = []
    for idx in range(args.start_index, args.end_index+1):
        fname = "{}.{}".format(args.prefix, idx)
        buf += json.load(open(fname))
    json.dump(buf, open(args.output, 'w'), indent='  ')


def main(args):
    if exists(args.output):
        open(args.output).close()
    if args.type == "json":
        merge_json(args)
    elif args.type == "txt":
        merge_text(args)


if __name__ == "__main__":
    main(parse_args())

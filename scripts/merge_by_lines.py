import argparse
from random import uniform, sample, seed


seed(141)


import codecs

def unescaped_str(arg_str):
        return codecs.decode(str(arg_str), 'unicode_escape')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_files", type=str, help="filenames split with : ")
    parser.add_argument("--d", type=unescaped_str, help="merge delimiter")
    parser.add_argument("--add_blank_line", action="store_true")
    return parser.parse_args()


def main(args):
    d = str(args.d)
    files = [open(fname) for fname in args.input_files.strip().split(":")]
    for lines in zip(*files):
        print(d.join([it.strip() for it in lines]))
        if args.add_blank_line:
            print()


if __name__ == "__main__":
    main(parse_args())

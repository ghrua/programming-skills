from random import sample
import json
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-src")
    parser.add_argument("-tgt")
    parser.add_argument("-consts")
    parser.add_argument("-vtarget")
    parser.add_argument("-n", type=int, help="num to sample")
    parser.add_argument("-out", help="output dir/basename")
    return parser.parse_args()


def load_text_file(fname):
    ans = []
    with open(fname) as f:
        for it in f:
            ans.append(it)
    return ans


def load_json_file(fname):
    with open(fname) as f:
        x = json.load(f)
    return x


def fetech_by_index(fcontent, idx_list):
    ans = []
    for it in idx_list:
        ans.append(fcontent[it])
    return ans


def dump_text_file(var, fname):
    with open(fname, 'w') as f:
        for it in var:
            f.write(it)


def dump_json_file(var, fname):
    with open(fname, 'w') as f:
        json.dump(var, f, indent='  ')


def main(args):
    # src
    fcontent = load_text_file(args.src)
    idx_list = sample(range(len(fcontent)), args.n)
    dump_text_file(fetech_by_index(fcontent, idx_list), args.out + '.src')
    # tgt
    fcontent = load_text_file(args.tgt)
    dump_text_file(fetech_by_index(fcontent, idx_list), args.out + '.tgt')
    # consts
    if args.consts:
        fcontent = load_json_file(args.consts)
        dump_json_file(fetech_by_index(fcontent, idx_list), args.out + '.consts')

    # vtarget
    if args.vtarget:
        fcontent = load_json_file(args.vtarget)
        dump_json_file(fetech_by_index(fcontent, idx_list), args.out + '.vtarget')


if __name__ == "__main__":
    args = parse_args()
    main(args)

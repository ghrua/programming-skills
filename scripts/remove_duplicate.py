import argparse
from tqdm import tqdm


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-src_md5")
    parser.add_argument("-tgt_md5")
    parser.add_argument("-out", help="output dir/basename")
    return parser.parse_args()


def main(args):
    fsrc = open(args.src_md5, 'r', encoding='utf-8')
    ftgt = open(args.tgt_md5, 'r', encoding='utf-8')
    funique = open(args.out + '.unique', 'w')
    fduplicate = open(args.out + '.duplicate', 'w')
    table = set()
    n = 1
    for src, tgt in tqdm(zip(fsrc, ftgt)):
        label = (src, tgt)
        if label in table:
            fduplicate.write("{}\n".format(n))
        else:
            table.add(label)
            funique.write("{}\n".format(n))
        n += 1


if __name__ == "__main__":
    args = parse_args()
    main(args)

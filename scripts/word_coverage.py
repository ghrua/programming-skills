import argparse
from collections import Counter
from tqdm import tqdm


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-fname")
    parser.add_argument("-topk", type=int, default=50000, help="Top k words in file")
    parser.add_argument("-vocab",  help="User provided vocab")
    return parser.parse_args()


def countByTopk(args):
    c = Counter()
    total_words = 0.0
    with open(args.fname, "r", encoding="utf-8") as fin:
        for line in tqdm(fin):
            sp_line = line.strip().split()
            c.update(sp_line)
            total_words += len(sp_line)
    cover_words = 0.0
    for it in c.most_common(args.topk):
        cover_words += it[1]
    print("{:.2f}% words in {} file is coverd by top {} words".format(cover_words / total_words * 100,
                                                                      args.fname,
                                                                      args.topk))


def countByVocab(args):
    total_words = 0.0
    cover_words = 0.0
    vocabSet = set()
    with open(args.vocab, "r", encoding="utf-8") as fin:
        for line in fin:
            vocabSet.add(line.strip())

    with open(args.fname, "r", encoding="utf-8") as fin:
        for line in tqdm(fin):
            sp_line = line.strip().split()
            total_words += len(sp_line)
            for word in sp_line:
                if word in vocabSet:
                    cover_words += 1
    print("{:.2f}% words in {} file is coverd by {}".format(cover_words / total_words * 100,
                                                            args.fname, args.vocab))


if __name__ == "__main__":
    args = parse_args()
    if args.vocab:
        countByVocab(args)
    else:
        countByTopk(args)

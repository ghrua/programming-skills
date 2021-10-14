import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fin", type=str)
    return parser.parse_args()


def main(args):
    n_words = 0.0
    n_sents = 0.0
    with open(args.fin) as fin:
        for line in fin:
            n_words += len(line.strip().split())
            n_sents += 1
    print("[Info] avg sent length: {:.2f}".format(n_words / n_sents))


if __name__ == "__main__":
    main(parse_args())

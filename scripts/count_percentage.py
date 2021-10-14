import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fin", type=str)
    parser.add_argument("--topk", type=int)
    return parser.parse_args()


def main(args):
    n, s = 0, 0
    with open(args.fin) as fin:
        for idx, line in enumerate(fin):
            _, cnt = line.strip().split('\t')
            cnt = int(cnt)
            if idx < args.topk:
                n += cnt
            s += cnt
    print("[Info] percent: {:.2f}%".format(n/s * 100))

if __name__ == "__main__":
    main(parse_args())

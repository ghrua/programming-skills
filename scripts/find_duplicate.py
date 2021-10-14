import argparse
from tqdm import tqdm


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-query_md5")
    parser.add_argument("-key_md5")
    parser.add_argument("-out", help="output file path.")
    return parser.parse_args()


def main(args):
    fout = open(args.out, 'w', encoding="utf-8")
    table = {}
    print("[Info] Loading key file...")
    with open(args.key_md5, 'r', encoding='utf-8') as kfile:
        for idx, key in enumerate(kfile):
            table[key.strip()] = idx+1
    print("[Info] Searching...")
    ans = {}
    with open(args.query_md5, 'r', encoding='utf-8') as qfile:
        n = 1
        for query in tqdm(qfile):
            query = query.strip()
            if query in table:
                qidx = table[query]
                if qidx in ans:
                    ans[qidx].append(str(n))
                else:
                    ans[qidx] = [str(n)]
            n += 1

    for k in sorted(ans.keys()):
        dup_idx = ans[k]
        fout.write("{}: {}\n".format(k, " ".join(dup_idx)))
    print("[Info] Finished...")


if __name__ == "__main__":
    args = parse_args()
    main(args)

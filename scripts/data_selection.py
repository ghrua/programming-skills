import argparse
import torch
import logging
from os import path

logger = logging.getLogger(__name__)


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scorepath", type=str, default="path to save the overall score")
    parser.add_argument("--type", type=str, default="overall")
    parser.add_argument("--src", type=str, default="src data")
    parser.add_argument("--seed", type=int, default=404)
    return parser


def flat(arr2d):
    ans = []
    for it in arr2d:
        ans.extend(it)
    return ans


def main(args):
    logger.info("Loading overall score...")
    scores = torch.load(args.scorepath)
    logger.info("{} instances loaded".format(len(scores)))
    n = len(scores)
    selected = sorted(scores)

    prefix = args.src
    new_src = "{}.{}".format(prefix, args.type)
    logger.info("Selected src data will be written to {}...".format(path.basename(new_src)))
    fout_src = open(new_src, 'w')
    ptr = 0
    with open(args.src) as fin_src:
        for idx, s in enumerate(fin_src):
            if idx == selected[ptr]:
                fout_src.write(s)
                ptr += 1
            if ptr == n:
                break
    fout_src.close()


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    main(args)

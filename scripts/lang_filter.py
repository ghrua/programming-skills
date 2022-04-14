"""
Following Facebook FAIR’s WMT19 News Translation Task Submission,
we process the newscrawl dataset of English in 4-steps:
1. Normalization by moses
2. Tokenization by moses
3. Filtering out sentences with wrong language id.
4. BPE with a pretrianed model
5. Split of train dev test
"""
import torch
import logging
import argparse
from tqdm import tqdm
from os.path import basename
import fasttext


logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", default="")
    parser.add_argument("--output_file", default="")
    parser.add_argument("--model_path", default="./lid.176.bin")
    parser.add_argument("--expected_lang", default="en")
    return parser.parse_args()


def main(args):
    model = fasttext.load_model(args.model_path)
    num_line, num_match = 0, 0
    with open(args.input_file) as fin, open(args.output_file, 'w') as fout:
        for line in tqdm(fin):
            res = model.predict(line.strip())
            pred_lang = res[0][0]
            if pred_lang.endswith(args.expected_lang):
                fout.write(line)
                num_match += 1
            num_line += 1

    n = num_line-num_match
    logger.info("{} ({:.2f}%) lines are filtered out".format(n, n/num_line*100))
                



if __name__ == "__main__":
    main(parse_args())

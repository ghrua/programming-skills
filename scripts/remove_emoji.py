import torch
import logging
import argparse
from tqdm import tqdm
from os.path import basename
import random
import os
import re


emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                        "]+", flags=re.UNICODE)


logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", default="")
    parser.add_argument("--output_file", default="")
    return parser.parse_args()



def main(args):
    with open(args.input_file) as fin, open(args.output_file, 'w') as fout:
        for line in fin:
            new_line = emoji_pattern.sub(r'', line)
            fout.write(new_line + "\n")


if __name__ == "__main__":
    main(parse_args())

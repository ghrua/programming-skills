import torch
import logging
import argparse
from tqdm import tqdm
from os.path import basename
import random
import os

logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", default="")
    parser.add_argument("--output_dir", default="")
    parser.add_argument("--valid_num", type=int, default=2000)
    parser.add_argument("--test_num", type=int, default=2000)
    return parser.parse_args()


def main(args):
    data = []
    with open(args.input_file) as fin:
        for line in fin:
            data.append(line)
    ids = list(range(len(data)))
    random.shuffle(ids)
    valid_ids = ids[:args.valid_num]
    test_ids = ids[args.valid_num:args.valid_num+args.test_num]
    train_ids = ids[args.valid_num+args.test_num:]
    
    if not os.path.exists(args.output_dir):
        logger.info("Making output dir")
        os.makedirs(args.output_dir)

    logger.info("Saving train file")
    with open(args.output_dir + "/train.txt", 'w') as fout:
        for i in train_ids:
            fout.write(data[i])
    
    logger.info("Saving valid file")
    with open(args.output_dir + "/valid.txt", 'w') as fout:
        for i in valid_ids:
            fout.write(data[i])
    
    logger.info("Saving test file")
    with open(args.output_dir + "/test.txt", 'w') as fout:
        for i in test_ids:
            fout.write(data[i])    

if __name__ == "__main__":
    main(parse_args())

import torch
import logging
import argparse
from tqdm import tqdm
from os.path import basename
import fastBPE


logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", default="")
    parser.add_argument("--output_file", default="")
    parser.add_argument("--codes_path", default="")
    parser.add_argument("--vocab_path", default="")
    parser.add_argument("--batch_size", type=int, default=2048)
    return parser.parse_args()


def main(args):
    model = fastBPE.fastBPE(args.codes_path, args.vocab_path)
    batch = []
    with open(args.input_file) as fin, open(args.output_file, 'w') as fout:
        for line in tqdm(fin):
            batch.append(line.strip())
            if len(batch) >= args.batch_size:
                res = model.apply(batch)
                for bpe_line in res:
                    fout.write(bpe_line + "\n")
                batch = []
    
        if batch:
            res = model.apply(batch)
            for bpe_line in res:
                fout.write(bpe_line + "\n")
            batch = []        

if __name__ == "__main__":
    main(parse_args())

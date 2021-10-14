import argparse
from collections import Counter, OrderedDict
from tqdm import tqdm


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-fname")
    parser.add_argument("-topk", type=int, default=50000, help="Top k words in file")
    parser.add_argument("-min_freq", type=int, default=0, help="min word freq to keep")
    parser.add_argument("-vocab",  help="User provided vocab")
    parser.add_argument("-out",  help="dir/base name of output")
    parser.add_argument("-collect_all_bpe", action="store_true",
                        help="collect all bpe or not")
    return parser.parse_args()


def dumpFreqs(freqs, fname):
    with open(fname, 'w', encoding="utf-8") as fout:
        for key, val in freqs.items():
            fout.write("{}\t{}\n".format(key, val))


def dumpVocab(vocab, fname):
    with open(fname, 'w', encoding="utf-8") as fout:
        for word in vocab:
            fout.write("{}\n".format(word))


def buildVocab(args):
    c = Counter()
    with open(args.fname, "r", encoding="utf-8") as fin:
        for line in tqdm(fin):
            sp_line = line.strip().split()
            c.update(sp_line)
    freqFname = args.out + ".word.freqs"
    print("[Info] dump freqs to {}".format(freqFname))
    dumpFreqs(OrderedDict(c.most_common()), freqFname)
    vocabList = loadVocabList(args.vocab)
    vocabSet = set(vocabList)
    outOfVocabList = []
    n = 0
    for it in c.most_common():
        if it[0] in vocabSet:
            n += 1
            continue
        if n < args.topk and it[1] >= args.min_freq:
            outOfVocabList.append(it[0])
        elif args.collect_all_bpe and it[0].endswith("@@"):
            outOfVocabList.append(it[0])
        n += 1

    print("[Info] {} words are out of".format(len(outOfVocabList)))

    outOfVocabFname = args.out + ".outof.vocab"
    dumpVocab(outOfVocabList, outOfVocabFname)
    print("[Info] dump out of vocab List to {}".format(outOfVocabFname))

    vocabList.extend(outOfVocabList)
    allVocabFname = args.out + ".all.vocab"
    print("[Info] dump new vocab list to {}".format(allVocabFname))
    dumpVocab(vocabList, allVocabFname)


def loadVocabList(vocabFname):
    vocabList = []
    if vocabFname:
        with open(vocabFname, "r", encoding="utf-8") as fin:
            for line in fin:
                vocabList.append(line.strip())
    return vocabList


if __name__ == "__main__":
    args = parse_args()
    buildVocab(args)

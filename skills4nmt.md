
&#x1F3B9; **Data Preprocessing With Moses**

[Scripts](https://github.com/marian-nmt/moses-scripts) are here, and [user manual](https://www.statmt.org/wmt08/baseline.html) is here

&#x1F3B9;  **Tutorial of GIZA++**

[Download Page](http://web.archive.org/web/20100221051856/http://code.google.com/p/giza-pp)

[GIZA++ Installation and Running Tutorial](https://okapiframework.org/wiki/index.php/GIZA%2B%2B_Installation_and_Running_Tutorial)

[GIZA++ | MGIZA++ - error: ‘insert’ was not declared in this scope [Solved]](http://jsbachvu.blogspot.com/2017/06/giza-mgiza-error-insert-was-not.html)


&#x1F3B9; **Quickly Prepare WMT14 ENDE**

```
brew install aria2 # this is for mac
pip install subword-nmt
echo -e "https://nlp.stanford.edu/projects/nmt/data/wmt14.en-de/train.en\nhttps://nlp.stanford.edu/projects/nmt/data/wmt14.en-de/train.de\nhttps://nlp.stanford.edu/projects/nmt/data/wmt14.en-de/newstest2013.en\nhttps://nlp.stanford.edu/projects/nmt/data/wmt14.en-de/newstest2013.de\nhttps://nlp.stanford.edu/projects/nmt/data/wmt14.en-de/newstest2014.en\nhttps://nlp.stanford.edu/projects/nmt/data/wmt14.en-de/newstest2014.de" > data-url.txt
aria2c -i url-list.txt
cat train.de train.en | subword-nmt learn-bpe -s 32000 -o code.32k # learn a shared vocabulary as in "Attention is All You Need"
subword-nmt apply-bpe -c code.32k < train.de > train.bpe32k.de
subword-nmt apply-bpe -c code.32k < train.en > train.bpe32k.en
subword-nmt apply-bpe -c code.32k < newstest2013.en > newstest2013.bpe32k.en
subword-nmt apply-bpe -c code.32k < newstest2013.de > newstest2013.bpe32k.de
subword-nmt apply-bpe -c code.32k < newstest2014.en > newstest2014.bpe32k.en
subword-nmt apply-bpe -c code.32k < newstest2014.de > newstest2014.bpe32k.de
```

&#x1F3B9; **Quickly Prepare WMT19 Language Model**

```
# Following Facebook FAIR’s WMT19 News Translation Task Submission,
# we process the newscrawl dataset of English in 4-steps:
# 1. Filtering out sentences with wrong language id. (Fasttext on raw data: https://github.com/facebookresearch/fastText/issues/495#issuecomment-384689827)
# 2. Normalization by moses
# 3. Tokenization by moses
# 4. BPE with a pretrianed model
# 5. Split of train dev test

DEST=/home/XXX
FIN=$DEST/data/newscrawl_wmt19/news.2019.en.shuffled.deduped
BPECODES=$DEST/data/newscrawl_wmt19/bpecodes
LANG=en

python lang_filter.py --input_file $FIN \
                   --output_file $FIN.langid \
                   --model_path $DEST/data/newscrawl_wmt19/lid.176.bin \
                   --expected_lang $LANG

perl moses-scripts/scripts/tokenizer/normalize-punctuation.perl -l $LANG < $FIN.langid > $FIN.langid.norm
perl moses-scripts/scripts/tokenizer/tokenizer.perl -l $LANG -threads 16 < $FIN.langid.norm > $FIN.langid.norm.tok

python fast_bpe.py --input_file $FIN.langid.norm.tok \
                   --output_file $FIN.langid.norm.tok.bpe \
                   --codes_path $DEST/wmt19.en/bpecodes \
                   --vocab_path $DEST/wmt19.en/dict.txt

perl moses-scripts/scripts/tokenizer/remove-non-printing-char.perl < $FIN.langid.norm.tok.bpe > $FIN.langid.norm.tok.bpe.print
                   
python split.py --input_file $FIN.langid.norm.tok.bpe.print \
                   --output_dir ./split \
```

&#x1F3B9; **Convert SGM to Txt**

Remember to install bs4 in advance.

```python
import argparse
from bs4 import BeautifulSoup


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sgm", type=str)
    parser.add_argument("--txt", type=str)
    return parser.parse_args()


def main(args):
    with open(args.sgm) as fsgm, open(args.txt, 'w') as ftxt:
        sgm_str = fsgm.read()
        sp = BeautifulSoup(sgm_str, features="html.parser")
        txt_str = sp.get_text()
        for it in txt_str.split("\n"):
            if not it:
                continue
            ftxt.write(it + '\n')
        

if __name__ == "__main__":
    main(parse_args())
```

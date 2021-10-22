
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

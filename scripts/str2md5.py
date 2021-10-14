# coding=utf8
import sys
import hashlib
import os
import json
import io

# ignores = ["，", "。", " ", "！", "？", "“", "”", "\"", ".", ",", "!", "?","|"]
CHINESE_PUNC = set([it for it in """ 。！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…﹏"""])
ENGLISH_PUNC = set([it for it in """!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~`]"""])
ignores = CHINESE_PUNC.union(ENGLISH_PUNC)


def get_str_md5(src):
    m = hashlib.md5()
    m.update(src.encode("utf-8"))
    return m.hexdigest()


def get_corpus_line_md5(str):
    str = str.lower().strip()

    for tag in ignores:
        str = str.replace(tag, "")
    return get_str_md5(str)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(sys.stderr, "usage: python str2md5.py input_file output_file")
        exit()
    file_name = os.path.basename(sys.argv[1])
    ext = os.path.splitext(sys.argv[1])[1]

    fp = io.open(sys.argv[2], "w", encoding='utf-8')
    for line in io.open(sys.argv[1], encoding='utf-8'):
        line = line.strip()
        fp.write(get_corpus_line_md5(line) + u"\n")
        # fp.write(get_str_md5(line) + u"\n")
    fp.close()

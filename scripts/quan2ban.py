import sys
import codecs
import QB

def main(args):
    """process chinese doc"""
    lines = codecs.open(args[0], 'r', 'utf8', 'ignore').readlines()
    out = codecs.open(args[1], 'w', 'utf8', 'ignore')
    for l in lines:
        l = l.strip('\n')
        if len(l) > 0:
            l = QB.stringQ2B(l)
        out.write(l + '\n')
        if l.find('\n')>=0:
            print l
            break

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

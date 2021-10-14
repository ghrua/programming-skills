from sys import argv

if __name__ == "__main__":
    writer = open(argv[3], 'w', encoding='utf-8')
    with open(argv[1], 'r', encoding='utf-8') as f1, \
            open(argv[2], 'r', encoding='utf-8') as f2:
                for l1, l2 in zip(f1, f2):
                    writer.write("{} ||| {}\n".format(l1.strip(), l2.strip()))
    writer.close()

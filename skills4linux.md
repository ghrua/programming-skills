&#x1F3B9;	**Extracting Float Point Number from String**

```shell
echo "2.5 test. test -50.8" | grep -Eo '[+-]?[0-9]+([.][0-9]+)?'
```
[Reference](https://unix.stackexchange.com/a/290978/301510)


&#x1F3B9; **Simple File Encryption**

```shell
openssl des3 -pbkdf2 -k $PASSWORD -in $FIN_RAW -out $FILE_CRPT  #encode
openssl des3 -pbkdf2 -d -k $PASSWORD -in $FILE_CRPT > $FOUT #decode
```
&#x1F3B9; **Merge Text File by Column**

```shell
paste file1.txt file2.txt -d ","  # -d should be a character
```

To prepare data for `fast_align`, you should run the following two commands:

```shell
paste file1.txt file2.txt -d $"\t" > file.merge.back  # make sure that tab is not contained in the files
sed 's/\t/ ||| /g'  file.merge.back >  file.merge
```
&#x1F3B9; **Print Specific Line from Huge Text File**


```shell
sed 'Nq;d' file.txt
```

[Reference](https://stackoverflow.com/a/14709477/5793660)


&#x1F3B9; **Reverse Lines' Words**

python script:

```python
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input")
    return parser.parse_args()


def main(args):
    with open(args.input) as fin:
        for line in fin:
            print(" ".join(line.strip().split()[::-1]))


if __name__ == "__main__":
    main(parse_args())

```

example:
```shell
input.txt:
a b
c d

output.txt:
b a
d c
```

&#x1F3B9; **Reverse Lines**

```shell
tac a.txt > b.txt
```

&#x1F3B9; **Delete Files by Regex**

[Reference](https://superuser.com/a/392896/1119261)

```shell
find . -name 'wmt18.de-en.de.tk.len.term.[0-9]' -delete
```

&#x1F3B9; **Contab**

[user mannul](https://crontab.guru/every-10-minutes)

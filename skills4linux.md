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


&#x1F3B9; **System File Encoding**

```
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
```

&#x1F3B9; **Randomly Select N Lines from A File**

```
shuf -n 1 $FILE
```

[reference](https://stackoverflow.com/a/448127)


&#x1F3B9; **Install Tmux on CentOS**

[reference](https://gist.github.com/suhlig/c8b8d70d33462a95d2b0307df5e40d64)

```bash
# Install tmux on rhel/centos 7

# install deps
yum install gcc kernel-devel make ncurses-devel

# DOWNLOAD SOURCES FOR LIBEVENT AND MAKE AND INSTALL
curl -OL https://github.com/libevent/libevent/releases/download/release-2.1.8-stable/libevent-2.1.8-stable.tar.gz
tar -xvzf libevent-2.1.8-stable.tar.gz
cd libevent-2.1.8-stable
./configure --prefix=/usr/local
make
sudo make install
cd ..

# DOWNLOAD SOURCES FOR TMUX AND MAKE AND INSTALL
curl -OL https://github.com/tmux/tmux/releases/download/2.7/tmux-2.7.tar.gz
tar -xvzf tmux-2.7.tar.gz
cd tmux-2.7
LDFLAGS="-L/usr/local/lib -Wl,-rpath=/usr/local/lib" ./configure --prefix=/usr/local
make
sudo make install
cd ..
```


&#x1F3B9; **Slicing A String**

```bash
echo "STRING" | cut -cN-M
```
where `N` and `M` are the start index and end index respectively.

[reference](https://stackabuse.com/substrings-in-bash/)

&#x1F3B9; **Storing Output To A Variable**

```
var=$(command-name-here)
```

[reference](https://www.cyberciti.biz/faq/unix-linux-bsd-appleosx-bash-assign-variable-command-output/)


&#x1F3B9; **Remove Files by Pattern**

```python
import os                                                                                                                                             

for root, dirnames, filenames in os.walk('./tmp'): 
    for f in filenames: 
        if "best" in f: 
            continue 
        else: 
            os.remove(os.path.join(root, f)) 
```

&#x1F3B9; ** Iterate through Files Sorted by Data **

```
for CKPT in `ls -rt $TEXT/checkpoint_*.pt`
do
    ...
done
```

&#x1F3B9; ** Get File Name From Path **

```
FILE="/home/vivek/lighttpd.tar.gz"
echo ${FILE##*/}
## another example ##
url="https://www.cyberciti.biz/files/mastering-vi-vim.pdf"
echo "${url##*/}"
```
[reference](https://www.cyberciti.biz/faq/bash-get-basename-of-filename-or-directory-name/)



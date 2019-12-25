&#x1F3B9;	**Extracting Float Point Number from String**

```shell
echo "2.5 test. test -50.8" | grep -Eo '[+-]?[0-9]+([.][0-9]+)?'
```
[Reference](https://unix.stackexchange.com/a/290978/301510)


&#x1F3B9; **Encryption**

```shell
openssl des3 -pbkdf2 -k $PASSWORD -in $FIN_RAW -out $FILE_CRPT  #encode
openssl des3 -pbkdf2 -d -k $PASSWORD -in $FILE_CRPT > $FOUT #decode
```

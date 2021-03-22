&#x1F3B9; **General Vim Settins**

[Reference](https://stackoverflow.com/a/234578/5793660)

```vim
filetype plugin indent on
" show existing tab with 4 spaces width
set tabstop=4
" when indenting with '>', use 4 spaces width
set shiftwidth=4
" On pressing tab, insert 4 spaces
set expandtab
" Remember position of last edit and return on reopen
if has("autocmd")
  au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
endif
```

&#x1F3B9; **Resize The Split Windows Size  to Equal**

```vim
c-w =
```

&#x1F3B9; **Put The Cursor in The Line Last Time You Closed The File**

add the below code to `.vimrc`
```vim
if has("autocmd")
  au BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$") | exe "normal! g`\"" | endif
endif
```

[reference](https://askubuntu.com/a/202077/620511)

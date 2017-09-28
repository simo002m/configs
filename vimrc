set tabstop=4

syntax on

set number
highlight linenr ctermfg=green

filetype plugin indent on

autocmd FileType python map <F5> :w !python3 <CR>
autocmd FileType sh map <F5> :w !bash <CR>
autocmd FileType tex map <F5> :w !pdflatex % <CR>

set laststatus=0

"For windows
set backspace=2

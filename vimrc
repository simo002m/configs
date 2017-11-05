set tabstop=4

syntax on
highlight linenr ctermfg=green

colorscheme asmdev

"Colors for autocompletetion
highlight Pmenu ctermfg=9 ctermbg=0

set number

filetype plugin indent on

autocmd FileType python map <F5> :w !python3 <CR>
autocmd FileType sh map <F5> :w !bash <CR>
autocmd FileType tex map <F5> :w !pdflatex % <CR>

"Start of the vim-plug manager
call plug#begin()
	
		Plug 'scrooloose/nerdtree'
		Plug 'flazz/vim-colorschemes'
		Plug 'valloric/youcompleteme'

call plug#end()
"End vim-plug manager

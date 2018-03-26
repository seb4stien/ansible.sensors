export TERM=xterm-256color

alias ls='ls --color'
alias ll='ls -l'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

# git aliases
alias ga='git add'
alias gs='git status'
alias gc='git commit'
alias gd='git diff'
alias gr='git fetch --all && git rebase'
alias gP='git push'
# /git

# prompt
parse_git_branch() {
	     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
     }
export PS1="\u@\h \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "
# /prompt

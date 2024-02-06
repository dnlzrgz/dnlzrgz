# Load Powerlevel10k
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Load nvm
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

# Load pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"

# Poetry
export PATH="$HOME/.local/bin:$PATH"

# Some personal config
export EDITOR="nvim"
export PATH=$HOME/bin:/usr/local/bin:$PATH

# OMZ installation.
export ZSH="$HOME/.oh-my-zsh"

# Theme
ZSH_THEME="powerlevel10k/powerlevel10k"

# Enable command auto-correction.
ENABLE_CORRECTION="true"

# Plugins
plugins=(git python poetry pyenv node nvm npm docker docker-compose)

source $ZSH/oh-my-zsh.sh

# Common aliases
alias vim="nvim"
alias reload="source ~/.zshrc"
alias cl="clear"
alias cls="clear"
alias :q="exit"

# `cd` aliases
alias ..="../.."
alias ...="../../.."
alias ....="../../../.."

alias projects="cd ~/projects"

# Config files aliases
alias zconf="nvim ~/.zshrc"
alias gconf="nvim ~/.gitconfig"
alias vconf="nvim ~/.config/nvim/init.lua"
alias tconf="nvim ~/.tmux.conf"

# Update related aliases
alias update="sudo apt update"
alias upgrade="sudo apt upgrade"
alias upgradey="sudo apt upgrade -y"
alias nvmup="nvm install node"
alias pyup="pyenv update"

# Poetry aliases
alias pon="poetry new"
alias poi="poetry init"
alias poa="poetry add"
alias poad="poetry add --group dev"
alias pos="poetry shell"
alias pou="poetry update"
alias posu="poetry self update"

# Docker aliases
alias dils="docker image ls"
alias dipr="docker image prune"
alias dcls="docker container ls"
alias dclsa="docker container ls -a"

# Tmux aliases
alias tn="tmux new -s $(pwd | sed 's/.*\///g')"
alias tls="tmux ls"
alias ta="tmux a"
alias tat="tmux a -t"

# Some utils aliases
alias gg="lazygit"
alias news="newsboat"

alias myip="curl https://ipinfo.io/json"
alias weather="curl wttr.in"

# Flip a coin
alias coin="python -c \"import random; print('Heads' if random.choice([True, False]) else 'Tails')\""

# Run `p10k configure`
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

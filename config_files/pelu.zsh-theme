function collapse_pwd {
    echo $(pwd | sed -e "s,^$HOME,~,")
}

local ret_status="%(?:%{$fg_bold[green]%}➜ :%{$fg_bold[red]%}➜ )"
PROMPT='${ret_status} %{$fg[cyan]%}${PWD/#$HOME/~}%{$reset_color%} $(git_prompt_info)'

ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg[white]%} (%{$fg[red]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%} "
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg[white]%}) %{$fg[red]%} "
ZSH_THEME_GIT_PROMPT_CLEAN="%{$fg[white]%}) %{$fg[yellow]%} "
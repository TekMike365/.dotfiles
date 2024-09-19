# My dotfiles

## Requirements

Ensure you have the following installed on your system

### Git (duh)

[git](https://git-scm.com/)

### GNU Stow

[stow](https://www.gnu.org/software/stow/stow.html)

```
sudo apt install stow
```

## Application configs

- [vim](https://github.com/vim/vim)
- [starship](https://starship.rs/)
- [kitty](https://sw.kovidgoyal.net/kitty/)
- [neovim](https://github.com/neovim/neovim) >0.8
    - [fd-find](https://github.com/sharkdp/fd)
    - [ripgrep](https://github.com/BurntSushi/ripgrep)
    - [lazygit](https://github.com/jesseduffield/lazygit) (optional)

## Installation

First, clone this repo to your $HOME directory

```
git clone git@github.com:TekMike365/.dotfiles.git
```

Then remove all config files that collide with the config files in this repo,
and create all config dirs.

Then cd into it and use GNU stow to create symlinks

```
cd .dotfiles
stow .
```


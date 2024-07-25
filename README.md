# My dotfiles

## Requirements

Ensure you have the following installed on your system

### Git (duh)

### GNU Stow
```
sudo apt install stow
```

## Installation

First, clone this repo to your $HOME directory

```
git clone git@github.com:TekMike365/.dotfiles.git
```

Then cd into it and use GNU stow to create symlinks

```
cd .dotfiles
stow .
```


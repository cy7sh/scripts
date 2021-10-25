#!/bin/bash

mkdir ~/configs
rm -rf ~/configs/awesome
mkdir ~/configs/awesome
cp -r ~/.config/awesome/* ~/configs/awesome
rm -rf ~/configs/nvim
mkdir ~/configs/nvim
cp -r ~/.config/nvim/* ~/configs/nvim
cp ~/.vimrc ~/configs
cp ~/.alacritty.yml ~/configs
cp ~/.tmux.conf ~/configs
cp ~/.Xmodmap ~/configs
cp ~/updateconf.sh ~/configs

cd ~/configs
git add .
if [ -z "$1" ]
then
	git commit -m "update configs"
else
	git commit -m "$1"
fi
git push
git push sh

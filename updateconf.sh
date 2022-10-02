#!/bin/bash

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
cp ~/.bashrc ~/configs
cp ~/.bash_profile ~/configs

cd ~/configs
git add .
if [ -z "$1" ]
then
	git commit -S -m "update configs"
else
	git commit -S -m "$1"
fi
git push
git push sh

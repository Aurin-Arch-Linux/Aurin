export SUDO_ASKPASS=${HOME}/.aurin/askpass.sh
cd $1
makepkg -si --noconfirm
rm -rf "$1"






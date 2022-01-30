export SUDO_ASKPASS=/opt/aurin/askpass.sh
cd $1
makepkg -si --noconfirm
rm -rf "$1"






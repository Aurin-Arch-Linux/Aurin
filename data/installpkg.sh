export SUDO_ASKPASS=/opt/aurin/askpass.sh
cd "$1" || exit 1 # Exit when an invalid directory is provided
makepkg -si --noconfirm

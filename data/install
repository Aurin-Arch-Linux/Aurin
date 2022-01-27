import os, subprocess, sys

if len(sys.argv) == 1:
   pkgname = "hello"
else:
   pkgname = str(sys.argv[1]).replace("aurin://","")

gitFormat = "https://aur.archlinux.org/{0}.git"

giturl = gitFormat.format(pkgname)
subprocess.run(["git", "clone", giturl, "/var/tmp/aurin/" + pkgname])
subprocess.run(["bash", "$HOME/.aurin/installpkg.sh", "/var/tmp/aurin/" + pkgname + "/"])
os.system('XDG_RUNTIME_DIR=/run/user/$(id -u) notify-send -i $HOME/.aurin/aurin48.png "Install Success"'+ ' ' + pkgname +'" has been installed."')




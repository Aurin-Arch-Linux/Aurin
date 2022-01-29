# Maintainer: Suleman Elahi <suleman@ilfrs.ga>
pkgname=Aurin
pkgver=0.1
pkgrel=1
pkgdesc="Aurin is AUR packages installer."
arch=("any")
url="https://github.com/suleman-elahi/Aurin"
license=('MIT')
depends=('libnotify' 'tk')
source=("git://github.com/suleman-elahi/${pkgname}/")
sha1sums=('SKIP')

package() {
    mkdir -p $pkgdir/$HOME/.aurin/
    install -D -m755 "$srcdir/Aurin/data/aurin.desktop" "$pkgdir/usr/share/applications/aurin.desktop"
    xdg-mime default aurin.desktop x-scheme-handler/aurin
    cp "$srcdir/Aurin/data/askpass.sh" "$HOME/.aurin/askpass.sh"
    install -D "$srcdir/Aurin/data/aurin.png" "$pkgdir/usr/share/icons/default/aurin.png"
    cp "$srcdir/Aurin/data/aurin48.png" "$HOME/.aurin/aurin48.png"
    cp "$srcdir/Aurin/data/installpkg.sh" "$HOME/.aurin/installpkg.sh"
    cp "$srcdir/Aurin/data/passprompt.py" "$HOME/.aurin/passprompt.py"
    cp "$srcdir/Aurin/data/install.py" "$HOME/.aurin/install.py"
    install -D -m755 "$srcdir/Aurin/data/aurin" "$pkgdir/usr/bin/aurin"
}

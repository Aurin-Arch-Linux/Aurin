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
    install -D -m755 "$srcdir/Aurin/data/askpass.sh" "$pkgdir/$HOME/.aurin/askpass.sh"
    install -D "$srcdir/Aurin/data/aurin.png" "$pkgdir/usr/share/icons/default/aurin.png"
    install -D "$srcdir/Aurin/data/aurin48.png" "$pkgdir/$HOME/.aurin/aurin48.png"
    install -D -m755 "$srcdir/Aurin/data/installpkg.sh" "$pkgdir/$HOME/.aurin/installpkg.sh"
    install -D -m755 "$srcdir/Aurin/data/passprompt.py" "$pkgdir/$HOME/.aurin/passprompt.py"
    install -D -m755 "$srcdir/Aurin/data/aurin" "$pkgdir/usr/bin/aurin"
}

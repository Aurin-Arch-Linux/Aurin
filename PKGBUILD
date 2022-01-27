# Maintainer: Suleman Elahi <suleman@ilfrs.ga>
pkgname=aurin
pkgver=0.1
pkgrel=1
pkgdesc="Aurin is AUR packages installer."
arch=("any")
url="https://github.com/suleman-elahi/aurin"
license=('MIT')
depends=('libnotify' 'tk')
source=("git://github.com/suleman-elahi/${pkgname}/")
sha1sums=('SKIP')

package() {
    xdg-mime default aurin.desktop x-scheme-handler/aurin
    mkdir -p $pkgdir/$HOME/.aurin/
    install -D -m755 ./data/aurin.desktop $pkgdir/usr/share/applications/
    xdg-mime default aurin.desktop x-scheme-handler/aurin
    install -D -m755 ./data/askpass $pkgdir/$HOME/.aurin/
    install -D -m755 ./data/aurin.png $pkgdir/$HOME/.aurin/
    install -D -m755 ./data/aurin48.png $pkgdir/$HOME/.aurin/
    install -D -m755 ./data/install $pkgdir/$HOME/.aurin/
    install -D -m755 ./data/installpkg.sh $pkgdir/$HOME/.aurin/
    install -D -m755 ./data/passprompt $pkgdir/$HOME/.aurin/
    install -D -m755 ./data/runner $pkgdir/$HOME/.aurin/
    make DESTDIR="$pkgdir/" install
}

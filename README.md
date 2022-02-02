<h1 align="center">
  <br>
  <a href="https://github.com/Suleman-Elahi/Aurin"><img src="https://raw.githubusercontent.com/Suleman-Elahi/Aurin/main/data/aurin.png" alt=" Aurin" width="200px"></a>
</h1>

<h4 align="center">A quick AUR installer for Arch Linux. Install packages from AUR website in a click. </h4>

<p align="center">
    <a href="https://github.com/Suleman-Elahi/Aurin/commits">
    <img src="https://img.shields.io/github/commit-status/suleman-elahi/aurin/main/39679543820c4e15c8f8f0e9e4b5a1de60fd4eb2"
         alt="GitHub last commit">
    <a href="https://github.com/Suleman-Elahi/Aurin/issues">
    <img src="https://img.shields.io/github/issues-raw/suleman-elahi/Aurin"
         alt="GitHub issues">
    <a href="https://github.com/Suleman-Elahi/Aurin/pulls">
    <img src="https://img.shields.io/github/issues-pr-raw/suleman-elahi/aurin"
         alt="GitHub pull requests">
    <a href="https://twitter.com/intent/tweet?text=Try%20a%20new%20weird%20AUR%20installer%3A%20https%3A//github.com/Suleman-Elahi/Aurin/">
    <img src="https://img.shields.io/twitter/url/https/github.com/ArmynC/ArminC-AutoExec.svg?style=flat-square&logo=twitter"
         alt="GitHub tweet">
</p>

<p align="center">
  <a href="#about">About</a> •
  <a href="#installation">Installation</a> •
  <a href="#features">Features</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#support">Support</a> •
  <a href="#license">License</a>
</p>

---

## About

<table>
<tr>
<td>

**Aurin** is a **non conventional** AUR packages installer that aims to **install AUR packages** in one click right from the AUR website. From package page, you can install it in a click just like you install browser extensions.

It comes with a simple background application that you have to install on your system along with helper Chrome/Firefox/Microsoft Edge exensions.

It **Adds Install button on View PKGBUILD page** of an AUR package. Click on the button to install any package quickly. It throws desktop notification when the package has installed successfully and deletes the intermediary files.
<p align="center">
<img src="https://raw.githubusercontent.com/Suleman-Elahi/Aurin/main/data/aurin-in-action.png">
<img src="https://raw.githubusercontent.com/Suleman-Elahi/Aurin/main/data/aurin-installed.png">
<img src="https://raw.githubusercontent.com/Suleman-Elahi/Aurin/main/data/aurin-sudo.png">  
</p>
<p align="right">
<sub>(Preview)</sub>
</p>

</td>
</tr>
</table>

## Installation

##### Downloading and installing steps:
* Open Terminal and type: `git clone https://github.com/Suleman-Elahi/Aurin/ && cd Aurin`
* Run `makepkg -si`
* Install the Chrome/Firefox helper extension for Aurin either from [here](https://github.com/Suleman-Elahi/Aurin/tree/main/Aurin_Extension) or from below.
  * **Microsoft Edge**: https://microsoftedge.microsoft.com/addons/detail/aurin/chbdgmakgdbpfjpbjnalknmkjcneicnk
  * **Firefox**: https://addons.mozilla.org/en-US/firefox/addon/aurin/
* Done
* Open any AUR package page, for example [hello](https://aur.archlinux.org/packages/hello). Click on "View PKGBUILD" link from the right side of the page and you will find the "Install" button.

## Features

|                            |       Aurin       |
| -------------------------- | :----------------:|
| Installl any package       |         ✔️        |
| Ask sudo password via GUI  |         ✔️        |
| Delete files after install |         ✔️        |
| Handle URLs                |         ✔️        |
| AUR Updates/deps resolve   |         ❌        |
| Lock system                |         ❌        |
| Loading indicator          |         ❌        |
| Submitted to AUR           |         ❌        |

## Contributing

Got **something interesting** you'd like to **share**? open a PR or suggest a feature by opening an issue.                                       |

## Support

Reach out to me via the **[profile addresses](https://github.com/Suleman-Elahi)**.

## Credits

Aurin Icon: https://www.reddit.com/r/archlinux/comments/g8iygf/arch_linux_logo_using_unicode_block_characters/

## License

[![License: MIT](https://img.shields.io/github/license/suleman-elahi/Aurin)](https://tldrlegal.com/license/mit-license)

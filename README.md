<h1 align="center">
  <br>
  <a href="https://github.com/Suleman-Elahi/Aurin"><img src="https://raw.githubusercontent.com/Suleman-Elahi/Aurin/main/data/aurin.png" alt=" Aurin"></a>
</h1>

<h4 align="center">A quick AUR installer for Arch Linux. Install packages from AUR website in a click. </h4>

<p align="center">
    <a href="https://github.com/Suleman-Elahi/Aurin/commits">
    <img src="https://img.shields.io/github/last-commit/ArmynC/ArminC-AutoExec.svg?style=flat-square&logo=github&logoColor=white"
         alt="GitHub last commit">
    <a href="https://github.com/Suleman-Elahi/Aurin/issues">
    <img src="https://img.shields.io/github/issues-raw/ArmynC/ArminC-AutoExec.svg?style=flat-square&logo=github&logoColor=white"
         alt="GitHub issues">
    <a href="https://github.com/Suleman-Elahi/Aurin/pulls">
    <img src="https://img.shields.io/github/issues-pr-raw/ArmynC/ArminC-AutoExec.svg?style=flat-square&logo=github&logoColor=white"
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

**Aurin** is a **non conventional** AUR packages installer that aims to **install AUR packages** in one click right from the AUR website. From package page, you can install it in a click just like you install browser addons.

It comes with a simple application that you have to install to on your system alogn woth helper Chrome/Frefox exensions.

It **Adds Install button on View PKGBUILD page** of an AUR package. Click on the button to install any package in a click. It throws desktop notification when the ackage has installed and deleted the intermediary files.
<p align="center">
<img src="https://raw.githubusercontent.com/Suleman-Elahi/Aurin/main/data/aurin-in-action.png"
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
  * **Microsoft Edge**: soon
  * **Firefox**: soon
* Done
* Open any AUR package page, for example [hello](https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=hello). Click on "View PKGBUILD" link and you will find the "Install" button.

## Features

|                            |       Aurin       |
| -------------------------- | :----------------:|
| Installl any package       |         ✔️         |
| Browse package             |        ❌         |
| Lock system                |        ❌         |
| Loading indicator          |        ❌         |
| Ask sudo password voa GUI  |         ✔️         |
| Delete files after install |         ✔️         |
| Handle URLs                |         ✔️         |

## Contributing

Got **something interesting** you'd like to **share**? open a PR or suggest a feature by opening an issue.                                       |

## Support

Reach out to me via the **[profile addresses](https://github.com/Suleman-Elahi)**.

## License

[![License: MIT](https://img.shields.io/github/license/suleman-elahi/Aurin)](https://tldrlegal.com/license/mit-license)

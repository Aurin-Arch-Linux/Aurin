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

if len(sys.argv) < 1:
    error_out(f"Invalid number of arguments, you must provide a package name")

input_pkg_name = sys.argv[1]

# Only accept input values that are an actual valid URI
if not input_pkg_name.startswith(URL_PREFIX):
    error_out(f"Input URL {input_pkg_name} does not start with {URL_PREFIX}")

# Use slicing to extract the package name.
pkg_name = input_pkg_name[len(URL_PREFIX):]

# Deny certain characters to avoid path pollution that can enable path traversal and such.
for thing in ILLEGAL_PKG_NAME_CONTENTS:
    if thing in pkg_name:
        error_out(f"Illegal character pattern {thing} in package name {pkg_name}")

# Make sure the temporary directory for aurin always exists
temp_dir.mkdir(parents=True, exist_ok=True)
build_root = temp_dir / pkg_name

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

os.chdir(os.environ.get("HOME", "/"))

shutil.rmtree(build_root, ignore_errors=True)

notify("/opt/aurin/aurin48.png", "Install Successful", f"{pkg_name} has been installed!")

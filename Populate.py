import sys

if (sys.version_info.major < 3):
    sys.stderr.write("Error: This version of Naomi requires Python 3.5 or greater\n")
    sys.exit(1)

import locale
try:
    encoding = locale.getpreferredencoding()
    if encoding and encoding.lower() not in ('utf-8', 'utf8'):
        sys.stderr.write("WARNING: Your system locale is configured to use a non-UTF-8 character encoding ({}).\n".format(encoding))
        sys.stderr.write("This may cause Naomi to crash when reading files or configuration containing international characters.\n")
        sys.stderr.write("Please consider setting your system locale to UTF-8 (e.g. by setting LC_ALL=en_US.UTF-8 in Linux).\n")
except Exception:
    # Ignore any errors during encoding check so startup doesn't fail
    pass

import naomi

naomi.main(args=["--repopulate"])


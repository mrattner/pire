import re
import sys


PACKAGE_REGEX = r"^[a-z0-9][_a-z0-9\-\.]+$"
package_name = "{{ cookiecutter.package_name }}"

if not re.match(PACKAGE_REGEX, package_name):
    print("ERROR: (%s) is not a valid NPM package name." % package_name)
    print("See https://www.npmjs.com/package/validate-npm-package-name")

    #Exit to cancel project
    sys.exit(1)


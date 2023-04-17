#!c:\python38\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ros2-keystroke==0.3.0','console_scripts','keystroke_arrows_to_twist'
__requires__ = 'ros2-keystroke==0.3.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('ros2-keystroke==0.3.0', 'console_scripts', 'keystroke_arrows_to_twist')()
    )

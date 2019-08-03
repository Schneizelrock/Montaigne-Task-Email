#!C:\Users\HP\PycharmProjects\flaskappemail\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'latest==0.4.1','console_scripts','latest'
__requires__ = 'latest==0.4.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('latest==0.4.1', 'console_scripts', 'latest')()
    )

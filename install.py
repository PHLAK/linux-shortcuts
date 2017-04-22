#!/usr/bin/env python3

from glob import glob
from shutil import copyfile

import argparse
import os

workingdir = os.path.dirname(os.path.realpath(__file__))
applications_dir = os.path.join(os.path.expanduser('~'), '.local/share/applications')
shortcuts = sorted(glob(os.path.join(workingdir, 'shortcuts/*.desktop')))

def installShortcut(path, promt=True):
    """Install a single shortcut"""

    basename = os.path.basename(path)
    shortcut = os.path.splitext(basename)[0]

    if (promt and os.path.isfile(os.path.join(applications_dir, basename))):
        while 'overwrite' not in locals() or overwrite.lower() not in ['y', 'n']:
            overwrite = input('A ' + shortcut + ' shortcut already exists, overwite it? [Y/N]: ')

        if (overwrite.lower() != 'y'):
            return

    print('Installing ' + shortcut + ' shortcut ... ', end='')
    copyfile(path, os.path.join(applications_dir, basename))
    print('DONE')

def installAllShortcuts(shortcuts, prompt=True):
    """Install all shortcuts"""

    for path in shortcuts:
        installShortcut(path, prompt)

    print('DONE')

def main():
    """Main execution function"""

    print('Which shortcut(s) would you like to install?')
    print('')

    print('   0: (all)')
    for index, value in enumerate(shortcuts):
        print('{index:4}: {value}'.format(
            index=index + 1,
            value=os.path.splitext(os.path.basename(value))[0]
        ))
    print('')

    while 'num' not in locals() or not num.isdigit() or not int(num) in range(0, len(shortcuts)):
        num = input('Number: ')

    print('')

    if (int(num) == 0):
        installAllShortcuts(shortcuts)
    else:
        installShortcut(shortcuts[int(num) - 1])

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Custom app shortcut installer for Linux')
    parser.add_argument('-a', '--all',
        help='Install (overwrite) all shortcuts',
        action='store_true',
        default=False
    )
    args = parser.parse_args()

    if args.all:
        installAllShortcuts(shortcuts, False)
    else:
        main()

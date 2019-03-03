import logging
import platform
from shutil import which
from subprocess import check_output

MACOS = not platform.mac_ver() == ('', ('', '', ''), '')


def get_open_name():
    commands = ['xdg-open', 'open']
    for command in commands:
        if which(command) is not None:
            return command


def get_default_browser():
    try:
        if not MACOS:
            return _get_linux_default_browser()
    except Exception as e:
        logging.debug(e)
        logging.info('Couldn\'t get the default browser.')


def _get_linux_default_browser():
    with open('/usr/share/applications/defaults.list', 'r') as system_defaults:
        for line in system_defaults:
            if 'x-scheme-handler/http' in line:
                default_value = line.split('=')[1]
                if ';' in default_value:
                    return default_value.split(';')[0].strip('.desktop')
                return default_value


def _get_macos_default_browser():
    return check_output('./macos_default_browser.sh')


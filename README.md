Linux Shortcuts
===============

Custom app shortcuts for Linux -- by, [Chris Kankiewicz](https://www.ChrisKankiewicz.com)

Introduction
------------

Run `install.py` to copy all shortcuts to `~/.local/share/applications/`

Adding a Shortcut
-----------------

You may add a shortcut by creating a new `.desktop` file in the `shortcuts`
folder. Use the following template for your shortcut.

    [Desktop Entry]
    Version=1.0
    Terminal=false
    Type=Application
    Name={{ APPLICATION_NAME }}
    Exec=google-chrome --app={{ APPLICATION_URL }}
    Icon={{ ICON_NAME }}
    StartupWMClass={{ STARTUP_WM_CLASS }}

When adding a new shortcut, to get the `StartupWMClass` of the window run
`xprop WM_CLASS` from a terminal then click on the window.

Troubleshooting
---------------

Please report bugs to the [GitHub Issue Tracker](https://github.com/PHLAK/chrome-apps/issues).

Copyright
---------

This project is licensed under the [MIT License](https://github.com/PHLAK/chrome-apps/blob/master/LICENSE).

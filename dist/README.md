# Packaging & Distribution

This section describes the necessary steps needed in order to package and distribute the SubStationGuard application to multiple platforms (Windows, macOS and Linux).

## Prerequisites

The software utilized for the packaging is **PyInstaller**.
**PyInstaller** is a cross-platform PyQt6 packaging system which supports building desktop applications for Windows, macOS and Linux. 
It automatically handles packaging of Python applications, along with any associated libraries and data files, either into a standalone one-file executable or a distributable folder that can then be used to create an installer.

PyInstaller works out of the box with PyQt6 and as of writing, current versions of PyInstaller are compatible with Python 3.6+. 

You can install PyInstaller using pip.

```
pip3 install PyInstaller
```

If you experience problems packaging your apps, your first step should always be to update your PyInstaller and hooks packages to the latest versions using:

```
pip3 install --upgrade PyInstaller pyinstaller-hooks-contrib
```

The hooks module contains specific packaging instructions and workarounds for common Python packages and is updated more regularly than PyInstaller itself.

## Windows

### Packaging

In order to package SubStationGuard application for Windows you need to follow the steps below:

1) Copy `dist/Windows/mainwindow.spec` to the same folder as the `mainwindow.py` (`gui/Mainwindow`)

2) Execute pyinstaller using the `.spec` file 

```
pyinstaller mainwindow.spec
```

3) An executable will be generated under a newly created folder here: `gui/Mainwindow/dist/SubStationGuard/SubStationGuard.exe`

> **Notes:**  
> The `build` folder is used by PyInstaller to collect and prepare files for bundling. It contains the results of analysis and additional logs. In most cases, you can ignore this folder unless you are debugging issues.
>
> The `dist` (short for "distribution") folder contains the files ready for distribution. This includes the application bundled as an executable, along with any associated libraries (e.g., PyQt6). Everything needed to run the application is included in this folder, so you can share the entire folder with others to run the app.


### Windows Installer

For the creation of a Windows Installer the tool called [InstallForge](https://installforge.net/) is utilized.
InstallForge is free and can be downloaded from [this page](https://installforge.net/download/)

The following setup is required to create the installer:

1) Package the application using `pyinstaller` and the steps mentioned above in Packaging

2) Update `[Build] -> File`, `[Files/Dirs]` and `[Folder]` paths to match the path of the cloned repo in your local filesystem

2) Open InstallForge and Open the `SubStationGuard.ifp`

3) Build the installer from InstallForge

## MacOS
Pending 

## Linux
Pending 
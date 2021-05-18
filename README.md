# blender_latex
Adds latex obejcts (curves) in blender

## Table of contents
* [Installation](#Installation)
* [Usage](#Usage)

## Installation
This has only been tested on Ubuntu with blender versoin 2.92.0.
It might work on Mac OS, and it probably won't on Windows. If you are interested in testing it out on 
Windows or Mac OS, please contact me.

You first need to install LaTeX. For Ubuntu, just run the command:
```
$ sudo apt-get install texlive-full
```

for Mac OS install.
```
$ brew install texlive 
```

Next, download the package from the green button on the upper right corner of this page, then 'Download ZIP'.
Unzip the file, go to blender > Edit > Preferences > Add-ons > Install... then find and select the addon_add_Latex_object.py file
that was unzipped.
Once you selected it, Check the box that appears 'Add Mesh: Add Blender Latex', then the add-on should be installed.

## Usage
In Blender (version 2.92.0), go to 'layout', and press Shift-T. A textbox will pop up, and type in your LaTeX command. 
Note that you have to type \\\ instead of \\. for exampole \\\Psi instead of \\Psi.

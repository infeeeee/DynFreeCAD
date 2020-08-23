# DynFreeCAD

Dynamo nodes for the FreeCAD API

**Early work in progress**, PRs are welcomed!

## Requirements

- Dynamo 2.7+. Download from [dynamobuilds.com](https://dynamobuilds.com/)

- FreeCAD built with python 3.7.
  
  - Download a prebuilt from here (0.18.3): [Release Win Py3.7 packaging experiments · sgrogan/FreeCAD · GitHub](https://github.com/sgrogan/FreeCAD/releases/tag/PY3.7-win)
  
  - You can build yourself a later verision, follow FreeCAD's doumentation

## Installation

- Clone this repo

- Open DynamoSandbox.exe

- Settings ➡ Manage Node and  Package Paths... ➡ Add the folder with ➕ ➡ Accept changes

## Usage and tips

Dynamo 2.7 added support for CPython 3.7, so FreeCAD can be called inside dynamo. Everything should work inside Python nodes, I want to add more common FreeCAD commands as nodes, so graphical programming can get a boost in FreeCAD.

### Initialize FreeCAD

Always start with these node. Add the path to the `bin` folder in the FreeCAD folder. After you initialized somewhere in the graph, you can simply use `import FreeCAD` in any nodes:

![Initialize](Screenshots/Initialize.png)

### Manage documents

If you want to update the list nodes, connect a Boolean node to the Run input, and change to True or False

![Documents](Screenshots/Documents.png)

### Python script

You can use the FreeCAD API in Python Script this way:

![Create Line](Screenshots/CreateLine.png)

This creates a line from a dynamo line in FreeCAD, than saves the document.

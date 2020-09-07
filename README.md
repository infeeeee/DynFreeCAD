# DynFreeCAD

Dynamo nodes for the FreeCAD API

**Early, work in progress**, PRs are welcomed!

## Requirements

- Dynamo 2.8+. Download from [dynamobuilds.com](https://dynamobuilds.com/)

- FreeCAD built with python 3.8.
  
  - Download a prebuilt from here (0.19): [Release FreeCAD Win Conda PY3.8 · sgrogan/FreeCAD · GitHub](https://github.com/sgrogan/FreeCAD/releases/tag/PY3.8)
  
  - You can build yourself a different verision, follow FreeCAD's doumentation

## Installation

- Clone this repo

- Open DynamoSandbox.exe

- Settings ➡ Manage Node and  Package Paths... ➡ Add a new folder with ➕, select the `Dyf` subfolder from where you cloned ➡ Accept changes

- (Dynamo package manager soon!)

### FreeCAD API in Dynamo

Dynamo 2.7 added support for CPython 3.7, so FreeCAD can be called inside dynamo. Everything should work inside Python nodes, I want to add more common FreeCAD commands as nodes, so graphical programming can get a boost in FreeCAD.

Unfortunately due to a bug in Dynamo 2.7, these nodes are only usable in 2.8 with Python 3.8. 

### Compatibility matrix

Table updated: 2020-09-07

| Dynamo | cPython in Dynamo | FreeCAD API | DynFreeCAD | Revit  |
| ------ | ----------------- | ----------- | ---------- | ------ |
| 2.6    | ❌                 | ❌           | ❌          | 2021.1 |
| 2.7    | 3.7               | ✔           | ❌          | ❌      |
| 2.8    | 3.8               | ✔           | ✔          | ❌      |
| 2.9    | 3.8               | ✔           | ✔          | ❌      |

## Usage and tips

⚠️ **As DynFreeCAD is under developement, it's possible that some screenshots are outdated** ⚠️

See `Examples` folder for some documents.

### Initialize FreeCAD and open or create a new document

Always start with these node. Add the path to the `bin` folder of FreeCAD. Connect the FreeCADModule ports!

![Initialize and open a document](Screenshots/Initialize+open.png)

### Manage documents

It's pretty straightforward how you have to manage documents with these nodes. For the `Refresh` and `Run` ports connect a boolean to update or run them. See `ManageDocuments.dyn` in the Examples folder.

![Documents](Screenshots/Documents.png)

### Manage properties

![Properties](Screenshots/Properties.png)

### Python script

You can use the FreeCAD API in Python Script this way:

![Create Line](Screenshots/CreateLine.png)

This creates a line from a dynamo line in FreeCAD, than saves the document.

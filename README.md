![](https://raw.githubusercontent.com/infeeeee/DynFreeCAD/master/Logo/DynFreeCAD_256.png) 

# DynFreeCAD

Dynamo nodes for the FreeCAD API

**Early, work in progress**, PRs are welcomed!

## Requirements

- Dynamo 2.8+. Download from [dynamobuilds.com](https://dynamobuilds.com/)

- FreeCAD built with python 3.8.
  
  - Download a prebuilt from here (0.19): [Release FreeCAD Win Conda PY3.8 · sgrogan/FreeCAD · GitHub](https://github.com/sgrogan/FreeCAD/releases/tag/PY3.8) The 'site_packages1' version works better.
  
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

<p align="center">
⚠️<b>As DynFreeCAD is under developement, it's possible that some screenshots and documentation are outdated</b>⚠️
</p>

Detailed documentation is in the [wiki](https://github.com/infeeeee/DynFreeCAD/wiki). 

See `Examples` folder for some Dynamo documents.

### Load the FreeCAD API

There is some bug in Dynamo, so you cannot load FreeCAD libs on later nodes, unless they were loaded in a first python node. So before using DynFreeCAD, you have to load libraries:

- Open `ApiLoader.dyn` from the Examples folder. 

- Click `Run`

- If no errors given, just close this graph. Do not close Dynamo, only close the graph!

- You can now start working with the FreeCAD api, create new graphs, or open other examples.

You have to do this every time you want to use the FreeCAD api in Dynamo. I hope sometimes this will be fixed, or at least I find a better workaround. 

Follow this forum thread for more info: [DynamoForum](https://forum.dynamobim.com/t/how-to-use-import-from-custom-path-in-multiple-cpython-blocks/55071)

### Open or create a new document

Always start with these nodes. Add the path to the `bin` folder of FreeCAD.

![Initialize and open a document](Screenshots/Initialize+open.png)

### Manage documents

Use the ouput of the OpenDocument or CreateDocument nodes output if you just work on one document. The bottom nodes just showing how these nodes are connectable. 

![Documents](Screenshots/Documents.png)

### Manage properties

![Properties](Screenshots/Properties.png)

### Python script

You can use the FreeCAD API in a Python Script this way:

![Api](Screenshots/Api.png)

See UseTheApi.dyn in Examples folder.

## Troubleshooting

If you have some problems, open an issue!

You can also ask questions on the related project's forums:

- [Dynamo Forum](https://forum.dynamobim.com/)
- [FreeCAD Forum](https://forum.freecadweb.org/)
- [OSArch Community](https://community.osarch.org/)

## Alternativ graphical programing interfaces for FreeCAD

- [GitHub - microelly2/NodeEditor: Node editor for FreeCAD with PyFLow](https://github.com/microelly2/NodeEditor)

- [GitHub - nortikin/sverchok: Sverchok](https://github.com/nortikin/sverchok) Blender addin with FreeCAD support

## License

MIT

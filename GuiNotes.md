# Notes about setting up FreeCAD gui

*This documentation is work in progress, it's possible that some required steps are missing.*

## 1. Install pip

Source: [Customizing Dynamo's Python 3 installation · DynamoDS/Dynamo Wiki · GitHub](https://github.com/DynamoDS/Dynamo/wiki/Customizing-Dynamo's-Python-3-installation)

This is just an extract, from this tutorial.

1. Download get-pip.py: [Installation - pip 20.2.4 documentation](https://pip.pypa.io/en/stable/installing/)
2. Copy it to: `%localappdata%\python-3.8.3-embed-amd64`
3. than:

```batch
cd %localappdata%\python-3.8.3-embed-amd64
echo import site>> python38._pth
.\python get-pip.py
```

## 2. Install PySide2

```batch
.\python .\Scripts\pip.exe install PySide2
```

## 3. Install and setup Pywin32

```batch
.\python .\Scripts\pip.exe install pywin32
.\python .\Scripts\pywin32_postinstall.py -install
```

## 4.  Other dependencies

It's possible that you will need this as well:

```batch

```

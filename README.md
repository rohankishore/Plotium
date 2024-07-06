<div align="center">

![banner!](https://github.com/rohankishore/Plotium/assets/109947257/f6593c70-96f0-457a-9bb1-3a91e1068849)
Plotium is a Python library designed for easy data visualization and analysis of chemical trends like Atomic Radii, Electronegativity, etc
</div>

<br>

- [📊 What can Plotium do?](#-what-can-plotium-do)
- [⬇️ Installation](#-installation)
- [🪴 Example Snippets](#-example-snippets)
   * [Example 1](#example-1)
   * [Example 2](#example-2)

## 📊 What can Plotium do?
Plotium provides graph plots of chemical trends of specific Groups, Types, Blocks, Periods, etc. You can view the graph in a window or attach it to a GUI using PyQt/PySide libraries.

<br>

# ⬇️ Installation

Plotium can be installed using PIP:

```bash
pip install Plotium
```

Or manually by installing the .tar.gz file from the [Releases](https://github.com/rohankishore/Plotium/releases)

<br>

# 🪴 Example Snippets

## Example 1

```python
from Plotium.Group.GROUP_1 import electronegativity

tp = electronegativity.plot()
tp.show()
```
![Figure_1](https://github.com/rohankishore/Plotium/assets/109947257/fa70136f-c3a7-453d-a262-3bc75cb5984f)

## Example 2

```python
from Plotium.Type.Actinoids import atomic_radius

tp = atomic_radius.plot()
tp.grid()
tp.show()
```
![Figure_1](https://github.com/rohankishore/Plotium/assets/109947257/15f973f6-5b5a-49c3-a6e9-2bcf6fb2a4e9)



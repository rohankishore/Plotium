<div align="center">

![banner!](https://github.com/rohankishore/Plotium/assets/109947257/f6593c70-96f0-457a-9bb1-3a91e1068849)

</div>

Plotium is a Python library designed for easy data visualization and analysis of chemical trends like Atomic Radii, Electronegativity, etc. Right now, 

<br>

# Table of Contents

- [📊 What can Plotium do?](#-what-can-plotium-do)
- [⬇️ Installation](#-installation)
- [🪴 Example Snippets](#-example-snippets)
   * [Example 1](#example-1)
- [🧩 Credits](#-credits)
 
<br>

## 📊 What can Plotium do?
Plotium provides graph plots of chemical trends of specific Groups, Types, Blocks, Periods, etc. You can view the graph in a window. ***Plotium can plot trends of***:
1. Electronegativity
2. Density
3. Atomic Radii
4. Melting Point
5. Boiling Point

***Divided into:***
1. Block Wise (S,P,D,F)
2. Types (Actinoids, Lanthanoids, etc)
3. Groups (1 - 18)
4. Periods (1 - 7)

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

***For more examples, check the [examples](https://github.com/rohankishore/Plotium/tree/main/examples) folder.***

# 🧩 Credits

The infos used in this project are from:
- [Periodic Trends - Chemistry Libre](https://chem.libretexts.org/Bookshelves/Inorganic_Chemistry/Supplemental_Modules_and_Websites_(Inorganic_Chemistry)/Descriptive_Chemistry/Periodic_Trends_of_Elemental_Properties/Periodic_Trends)
- [Britannica](https://www.britannica.com/)

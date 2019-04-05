# jupyter_freecad_kernel
A FreeCAD Kernel for Jupyter

## Dependencies
1. [FreeCAD](http://www.freecadweb.org/)
2. [Jupter](http://jupyter.org/)
3. for the examples (sympy, pydy, numpy, matplotlib)

## Installation
1. clone this repository (git clone https://github.com/looooo/jupyter_freecad_kernel)
2. run "jupyter kernelspec install /path/to/FreeCAD_kernel" (withoud trailing "/")
3. make the freecadkernel.py python importable (copy/link it to a place python can find it)
4. Depending on your FreeCAD version, you may need to install ipykernel for Python 2 with e.g. `pip2 install --user ipykernel`
5. Depending on your FreeCAD version, you may have to edit `~/.local/share/jupyter/kernels/freecad_kernel/freecadkernel.py` and replace `os.environ["QT_API"] = "pyside"` with `s.environ["QT_API"] = "pyside2"`.
6. Depending on your installation and FreeCAD version, you may have to edit `~/.local/share/jupyter/kernels/freecad_kernel/kernel.json` and replace both occurences of `python` with `python2`.

## Get started
1. start jupyter-notebook
2. navigate to the example directory and open RotationBox1.ipynb
3. wait for some time (the FreeCAD Gui will show up)
4. open RotationBox1.ipynb in FreeCAD
5. Now you have direct access to FreeCAD... run the cells

## Things to do
1. Store some information to couple FreeCAD Documents and Notebooks

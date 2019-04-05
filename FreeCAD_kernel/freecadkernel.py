import sys
import os
from ipykernel.ipkernel import IPythonKernel as Kernel

os.environ["QT_API"] = "pyside"

class FreeCADKernel(Kernel):
    implementation = 'FreeCAD'
    implementation_version = '0.1'
    banner = "notebook conection to freecad"

    def start(self):
        Kernel.start(self)
        self.do_execute("%gui qt", False)
        if os.path.exists('/usr/lib/freecad/lib/'):
            sys.path.append('/usr/lib/freecad/lib/')
        elif os.path.exists('/usr/lib/freecad-daily/lib/'):
            sys.path.append('/usr/lib/freecad-daily/lib/')
        else:
            raise RuntimeError('Cannot find FreeCAD libraries')
        import FreeCADGui
        self.win = FreeCADGui.showMainWindow()


if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=FreeCADKernel)

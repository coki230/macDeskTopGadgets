import sh

# print(sh.pwd())
# sh.rsync(['-r', '/Users/Coki_Zhao/Desktop/code/py/macDeskTopGadgets/.buildozer/osx/app/', '/Users/Coki_Zhao/Desktop/code/py/macDeskTopGadgets/.buildozer/osx/platform/kivy-sdk-packager-master/osx/myapp.app/Contents/Resources/yourapp'], _pgrp=False)

sh.rsync(['-rz', '/Users/Coki_Zhao/Desktop/temp/cp1', '/Users/Coki_Zhao/Desktop/temp/cp2'])


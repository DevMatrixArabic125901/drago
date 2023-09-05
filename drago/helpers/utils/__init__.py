from .extdl import *
from .paste import *

flag = True
check = 0
while flag:
    try:
        from . import format as _format
        from . import tools as _matrixtools
        from . import utils as _matrixutils
        from .events import *
        from .format import *

        break
    except ModuleNotFoundError as e:
        install_pip(e.name)
        check += 1
        if check > 5:
            break

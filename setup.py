import os
import sys

import cx_Freeze

sys.path.append(os.path.abspath(os.path.join(os.curdir, "src")))

executables = [cx_Freeze.Executable("src/tutorial.py")]

cx_Freeze.setup(
    name="Tutorial",
    options={
        'build_exe': {
            'packages': ["pygame", "game"],
            'include_files': ["res"]
        }
    },
    executables=executables,
)
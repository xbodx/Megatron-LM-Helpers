from setuptools import setup

from pybind11.setup_helpers import Pybind11Extension, build_ext
from pybind11 import get_cmake_dir

import sys

__version__ = "0.0.1"

ext_modules = [
    Pybind11Extension(
        "megatron_lm_helpers",
        ["src/helpers.cpp"],
        define_macros = [('VERSION_INFO', __version__)],
    ),
]

setup(
    name="megatron_lm_helpers",
    version=__version__,
    author="Roman Kasovsky",
    author_email="roman@kasovsky.ru",
    url="https://github.com/xbodx/helpers",
    description="Megatron-LM helpers",
    long_description="",
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    install_requires=["pybind11"],
    setup_requires=["pybind11"],    
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)
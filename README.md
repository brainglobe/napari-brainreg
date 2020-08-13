# napari-brainreg

[![License](https://img.shields.io/pypi/l/napari-brainreg.svg?color=green)](https://github.com/napari/napari-brainreg/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-brainreg.svg?color=green)](https://pypi.org/project/napari-brainreg)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-brainreg.svg?color=green)](https://python.org)
[![tests](https://github.com/brainglobe/napari-brainreg/workflows/tests/badge.svg)](https://github.com/adamltyson/napari-brainreg/actions)
[![codecov](https://codecov.io/gh/brainglobe/napari-brainreg/branch/master/graph/badge.svg)](https://codecov.io/gh/adamltyson/napari-brainreg)

Visualise [brainreg](https://github.com/brainglobe/brainreg) registration output in [napari](https://github.com/napari/napari)

Based on the [napari cookiecutter plugin template](https://github.com/napari/cookiecutter-napari-plugin) and [napari-ndtiffs](https://github.com/tlambert03/napari-ndtiffs) by [@tlambert03](https://github.com/tlambert03)

----------------------------------

## Installation
Assuming you already have [napari](https://github.com/napari/napari) installed, you can install `napari-brainreg` via pip:

    pip install napari-brainreg

## Usage
Open napari and drag your [brainreg](https://github.com/brainglobe/brainreg) output directory (the one with the log file) onto the napari window.
    
Various images should then open, including:
* `Image (downsampled)` - the image used for registration
* `Annotations` - the atlas labels, warped to your sample brain
* `Boundaries` - the boundaries of the atlas regions

If you downsampled additional channels, these will also be loaded.

![process](https://raw.githubusercontent.com/brainglobe/napari-brainreg/master/resources/napari-brainreg.png)

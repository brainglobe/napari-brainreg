# napari-brainreg
### This tool is no longer under development, please use [brainglobe-napari-io](https://github.com/brainglobe/brainglobe-napari-io) instead

[![License](https://img.shields.io/pypi/l/napari-brainreg.svg?color=green)](https://github.com/brainglobe/napari-brainreg/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-brainreg.svg?color=green)](https://pypi.org/project/napari-brainreg)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-brainreg.svg?color=green)](https://python.org)
[![tests](https://github.com/brainglobe/napari-brainreg/workflows/tests/badge.svg)](https://github.com/brainglobe/napari-brainreg/actions)
[![Development Status](https://img.shields.io/pypi/status/napari-brainreg.svg)](https://github.com/brainglobe/napari-brainreg)
[![codecov](https://codecov.io/gh/brainglobe/napari-brainreg/branch/master/graph/badge.svg)](https://codecov.io/gh/brainglobe/napari-brainreg)
[![Gitter](https://badges.gitter.im/cellfinder/brainreg.svg)](https://gitter.im/cellfinder/brainreg?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

Visualise [brainreg](https://github.com/brainglobe/brainreg) registration output in [napari](https://github.com/napari/napari)

Based on the [napari cookiecutter plugin template](https://github.com/napari/cookiecutter-napari-plugin) and [napari-ndtiffs](https://github.com/tlambert03/napari-ndtiffs) by [@tlambert03](https://github.com/tlambert03)

----------------------------------

## Installation
Assuming you already have [napari](https://github.com/napari/napari) installed, you can install `napari-brainreg` via pip:

    pip install napari-brainreg

## Usage
#### Sample space
Open napari and drag your [brainreg](https://github.com/brainglobe/brainreg) output directory (the one with the log file) onto the napari window.
    
Various images should then open, including:
* `Registered image` - the image used for registration, downsampled to atlas resolution
* `atlas_name` - e.g. `allen_mouse_25um` the atlas labels, warped to your sample brain
* `Boundaries` - the boundaries of the atlas regions

If you downsampled additional channels, these will also be loaded.

Most of these images will not be visible by default. Click the little eye icon to toggle visibility.

_N.B. If you use a high resolution atlas (such as `allen_mouse_10um`), then the files can take a little while to load._

![sample_space](https://raw.githubusercontent.com/brainglobe/napari-brainreg/master/resources/sample_space.gif)


#### Atlas space
`napari-brainreg` also comes with an additional plugin, for visualising your data 
in atlas space. 

This is typically only used in other software, but you can enable it yourself:
* Open napari
* Navigate to `Plugins` -> `Plugin Call Order`
* In the `Plugin Sorter` window, select `napari_get_reader` from the `select hook...` dropdown box
* Drag `brainreg_standard` (the atlas space viewer plugin) above `brainreg` (the normal plugin) to ensure that the atlas space plugin is used preferentially.

![atlas_space](https://raw.githubusercontent.com/brainglobe/napari-brainreg/master/resources/atlas_space.gif)

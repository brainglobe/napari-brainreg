"""
This module is an example of a barebones numpy reader plugin for napari.

It implements the ``napari_get_reader`` hook specification, (to create
a reader plugin) but your plugin may choose to implement any of the hook
specifications offered by napari.
see: https://napari.org/docs/plugins/hook_specifications.html

Replace code below accordingly.  For complete documentation see:
https://napari.org/docs/plugins/for_plugin_developers.html

Adapted from napari-ndtiffs by @tlambert03
"""
import os
import imio
from napari_plugin_engine import napari_hook_implementation


@napari_hook_implementation
def napari_get_reader(path):
    """A basic implementation of the napari_get_reader hook specification.

    Parameters
    ----------
    path : str or list of str
        Path to file, or list of paths.

    Returns
    -------
    function or None
        If the path is a recognized format, return a function that accepts the
        same path or list of paths, and returns a list of layer data tuples.
    """

    if isinstance(path, str) and is_brainreg_dir(path):
        return reader_function


def is_brainreg_dir(path):
    path = os.path.abspath(path)
    if os.path.isdir(path):
        filelist = os.listdir(path)
    else:
        return False
    for fname in filelist:
        if fname.endswith(".log") and fname.startswith("brainreg"):
            return True
    return False


def reader_function(path):
    """Take a path or list of paths and return a list of LayerData tuples.

    Readers are expected to return data as a list of tuples, where each tuple
    is (data, [add_kwargs, [layer_type]]), "add_kwargs" and "layer_type" are
    both optional.

    Parameters
    ----------
    path : str or list of str
        Path to file, or list of paths.

    Returns
    -------
    layer_data : list of tuples
        A list of LayerData tuples where each tuple in the list contains
        (data, metadata, layer_type), where data is a numpy array, metadata is
        a dict of keyword arguments for the corresponding viewer.add_* method
        in napari, and layer_type is a lower-case string naming the type of layer.
        Both "meta", and "layer_type" are optional. napari will default to
        layer_type=="image" if not provided
    """

    print("Loading brainreg directory")
    path = os.path.abspath(path)
    downsampled = imio.load_any(os.path.join(path, "downsampled.tiff"))
    boundaries = imio.load_any(os.path.join(path, "boundaries.tiff"))
    annotations = imio.load_any(os.path.join(path, "registered_atlas.tiff"))
    return [
        (downsampled, {"name": "Downsampled image"}, "image"),
        (
            annotations,
            {"name": "Annotations", "blending": "additive", "opacity": 0.3},
            "labels",
        ),
        (
            boundaries,
            {"name": "Boundaries", "blending": "additive", "opacity": 0.5},
            "image",
        ),
    ]

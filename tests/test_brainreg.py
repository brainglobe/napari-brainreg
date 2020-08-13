from pathlib import Path
from napari_brainreg import napari_get_reader

data_dir = str(Path(__file__).resolve().parent / "data")
# TODO: Test data loaded is correct


def test_reader():
    # try to read data
    reader = napari_get_reader(str(data_dir))
    assert callable(reader)

    # make sure we're delivering the right format
    layer_data_list = reader(data_dir)
    assert isinstance(layer_data_list, list) and len(layer_data_list) > 0
    layer_data_tuple = layer_data_list[0]
    assert isinstance(layer_data_tuple, tuple) and len(layer_data_tuple) > 0


def test_get_reader_pass():
    reader = napari_get_reader("fake.file")
    assert reader is None

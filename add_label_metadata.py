# this assumes that we have copied the segmentation already!
import zarr

path = './data/em-raw.ome.zarr'

root = 'labels'
cells = 'labels/cells'


def add_root_metadata():
    with zarr.open(path, mode='a') as f:
        g = f[root]
        g.attrs.update({
            'labels':  ['cells']
        })


def add_label_metadata():

    # we don't write color metadata
    image_labels = {
        "version": "0.1",
        "source": {
            "image": "../../"
        }
    }

    with zarr.open(path, mode='a') as f:
        g = f[cells]
        g.attrs.update({
            'image_label': image_labels
        })


# add_root_metadata()
add_label_metadata()

import os

from detectron2.data.datasets.builtin_meta import _get_builtin_metadata
from detectron2.data.datasets.coco import register_coco_instances

from .ovis import _get_ovis_instances_meta
from .refcoco import (
    register_refcoco,
    _get_refcoco_meta,
)

from vita.data.datasets.ytvis import (
    register_ytvis_instances,
    _get_ytvis_2019_instances_meta,
    _get_ytvis_2021_instances_meta
)



from .mevis import register_mevis_instances

# ==== Predefined splits for REFCOCO datasets ===========
_PREDEFINED_SPLITS_REFCOCO = {
    # refcoco
    "refcoco-unc-train": ("coco/train2014", "annotations/refcoco-unc/instances_train.json"),
    "refcoco-unc-val": ("coco/train2014", "annotations/refcoco-unc/instances_val.json"),
    "refcoco-unc-testA": ("coco/train2014", "annotations/refcoco-unc/instances_testA.json"),
    "refcoco-unc-testB": ("coco/train2014", "annotations/refcoco-unc/instances_testB.json"),
    # refcocog
    "refcocog-umd-train": ("coco/train2014", "annotations/refcocog-umd/instances_train.json"),
    "refcocog-umd-val": ("coco/train2014", "annotations/refcocog-umd/instances_val.json"),
    "refcocog-umd-test": ("coco/train2014", "annotations/refcocog-umd/instances_test.json"),
    "refcocog-google-val": ("coco/train2014", "annotations/refcocog-google/instances_val.json"),
    # refcoco+
    "refcocoplus-unc-train": ("coco/train2014", "annotations/refcocoplus-unc/instances_train.json"),
    "refcocoplus-unc-val": ("coco/train2014", "annotations/refcocoplus-unc/instances_val.json"),
    "refcocoplus-unc-testA": ("coco/train2014", "annotations/refcocoplus-unc/instances_testA.json"),
    "refcocoplus-unc-testB": ("coco/train2014", "annotations/refcocoplus-unc/instances_testB.json"),
    # mixed
    "refcoco-mixed": ("coco/train2014", "annotations/refcoco-mixed/instances_train.json"),
    "refcoco-mixed-filter": ("coco/train2014", "annotations/refcoco-mixed/instances_train_filter.json"),
}

# ====    Predefined splits for mevis    ===========
_PREDEFINED_SPLITS_mevis = {
    "mevis_train": ("mevis/train",
                   "mevis/train/meta_expressions.json"),
    "mevis_dummy": ("mevis/dummy",
                     "mevis/dummy/meta_expressions.json"),
    "mevis_val": ("mevis/valid",
                 "mevis/valid/meta_expressions.json"),
    "mevis_test": ("mevis/test",
                  "mevis/test/meta_expressions.json"),
    "mevis_val_single": ("mevis/valid_single",
                 "mevis/valid_single/meta_expressions.json"),
}

_PREDEFINED_SPLITS_REFYTBVOS = {
    "rvos-refcoco-mixed": ("coco/train2014", "annotations/refcoco-mixed/instances_train_video.json"),
    "refyt_train": ("ref-youtube-vos/train/JPEGImages", "ref-youtube-vos/train.json"),
    "refyt_val": ("ref-youtube-vos/valid/JPEGImages", "ref-youtube-vos/valid.json"),
    "refdavis-val-0": ("ref-davis/valid/JPEGImages", "ref-davis/valid_0.json"),
    "refdavis-val-1": ("ref-davis/valid/JPEGImages", "ref-davis/valid_1.json"),
    "refdavis-val-2": ("ref-davis/valid/JPEGImages", "ref-davis/valid_2.json"),
    "refdavis-val-3": ("ref-davis/valid/JPEGImages", "ref-davis/valid_3.json"),
}

# ==== Predefined splits for YTVIS 2019 ===========
_PREDEFINED_SPLITS_YTVIS_2019 = {
    "ytvis_2019_train": ("ytvis_2019/train/JPEGImages",
                         "ytvis_2019/train.json"),
    "ytvis_2019_val": ("ytvis_2019/valid/JPEGImages",
                       "ytvis_2019/valid.json"),
    "ytvis_2019_test": ("ytvis_2019/test/JPEGImages",
                        "ytvis_2019/test.json"),
    "ytvis_2019_val_all_frames": ("ytvis_2019/valid_all_frames/JPEGImages",
                        "ytvis_2019/valid_all_frames.json"),
}


# ==== Predefined splits for YTVIS 2021 ===========
_PREDEFINED_SPLITS_YTVIS_2021 = {
    "ytvis_2021_train": ("ytvis_2021/train/JPEGImages",
                         "ytvis_2021/train.json"),
    "ytvis_2021_val": ("ytvis_2021/valid/JPEGImages",
                       "ytvis_2021/valid.json"),
    "ytvis_2021_test": ("ytvis_2021/test/JPEGImages",
                        "ytvis_2021/test.json"),
}


# ====    Predefined splits for OVIS    ===========
_PREDEFINED_SPLITS_OVIS = {
    "ovis_train": ("ovis/train",
                   "ovis/annotations/train.json"),
    "ovis_val": ("ovis/valid",
                 "ovis/annotations/valid.json"),
    "ovis_test": ("ovis/test",
                  "ovis/annotations/test.json"),
}


_PREDEFINED_SPLITS_COCO_VIDEO = {
    "coco2ytvis2019_train": ("coco/train2017", "coco/annotations/coco2ytvis2019_train.json"),
    "coco2ytvis2019_val": ("coco/val2017", "coco/annotations/coco2ytvis2019_val.json"),
    "coco2ytvis2021_train": ("coco/train2017", "coco/annotations/coco2ytvis2021_train.json"),
    "coco2ytvis2021_val": ("coco/val2017", "coco/annotations/coco2ytvis2021_val.json"),
    "coco2ovis_train": ("coco/train2017", "coco/annotations/coco2ovis_train.json"),
    "coco2ovis_val": ("coco/val2017", "coco/annotations/coco2ovis_val.json"),
}

def register_all_refcoco(root):
    for key, (image_root, json_file) in _PREDEFINED_SPLITS_REFCOCO.items():
        # Assume pre-defined datasets live in `./datasets`.
        register_refcoco(
            key,
            _get_refcoco_meta(),
            os.path.join(root, json_file) if "://" not in json_file else json_file,
            os.path.join(root, image_root),
        )

def register_all_mevis(root):
    for key, (image_root, json_file) in _PREDEFINED_SPLITS_mevis.items():
        # Assume pre-defined datasets live in `./datasets`.
        register_mevis_instances(
            key,
            os.path.join(root, json_file) if "://" not in json_file else json_file,
            os.path.join(root, image_root),
        )

def register_all_refytbvos_videos(root):
    for key, (image_root, json_file) in _PREDEFINED_SPLITS_REFYTBVOS.items():
        # Assume pre-defined datasets live in `./datasets`.
        register_ytvis_instances(
            key,
            _get_refcoco_meta(),
            os.path.join(root, json_file) if "://" not in json_file else json_file,
            os.path.join(root, image_root),
            has_expression=True
        )


def register_all_ytvis_2019(root):
    for key, (image_root, json_file) in _PREDEFINED_SPLITS_YTVIS_2019.items():
        # Assume pre-defined datasets live in `./datasets`.
        register_ytvis_instances(
            key,
            _get_ytvis_2019_instances_meta(),
            os.path.join(root, json_file) if "://" not in json_file else json_file,
            os.path.join(root, image_root),
        )


def register_all_ytvis_2021(root):
    for key, (image_root, json_file) in _PREDEFINED_SPLITS_YTVIS_2021.items():
        # Assume pre-defined datasets live in `./datasets`.
        register_ytvis_instances(
            key,
            _get_ytvis_2021_instances_meta(),
            os.path.join(root, json_file) if "://" not in json_file else json_file,
            os.path.join(root, image_root),
        )


def register_all_coco_video(root):
    for key, (image_root, json_file) in _PREDEFINED_SPLITS_COCO_VIDEO.items():
        # Assume pre-defined datasets live in `./datasets`.
        register_coco_instances(
            key,
            _get_builtin_metadata("coco"),
            os.path.join(root, json_file) if "://" not in json_file else json_file,
            os.path.join(root, image_root),
        )


def register_all_ovis(root):
    for key, (image_root, json_file) in _PREDEFINED_SPLITS_OVIS.items():
        # Assume pre-defined datasets live in `./datasets`.
        register_ytvis_instances(
            key,
            _get_ovis_instances_meta(),
            os.path.join(root, json_file) if "://" not in json_file else json_file,
            os.path.join(root, image_root),
        )


if __name__.endswith(".builtin"):
    # Assume pre-defined datasets live in `./datasets`.
    _root = os.getenv("DETECTRON2_DATASETS", "datasets")
    register_all_mevis(_root)
    register_all_ovis(_root)
    register_all_ytvis_2019(_root)
    register_all_ytvis_2021(_root)
    register_all_coco_video(_root)
    register_all_refytbvos_videos(_root)
    register_all_refcoco(_root)

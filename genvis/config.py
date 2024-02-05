# -*- coding: utf-8 -*-
from detectron2.config import CfgNode as CN


def add_genvis_config(cfg):
    cfg.MODEL.GENVIS = CN()
    cfg.MODEL.GENVIS.LEN_CLIP_WINDOW = 5
    cfg.MODEL.GENVIS.TEXT_HIDDEN_DIM = 256
    cfg.MODEL.GENVIS.BERT_DIM = 768
    cfg.MODEL.GENVIS.FREEZE_TEXT_ENCODER = True
    cfg.MODEL.GENVIS.FREEZE_GENVIS = True
    cfg.MODEL.GENVIS.FUSION_MASK_WEIGHT = 5.0
    cfg.MODEL.GENVIS.FUSION_DICE_WEIGHT = 3.0
    cfg.MODEL.GENVIS.GROUNDING_WEIGHT = 20.0
    cfg.MODEL.GENVIS.PROJ_LAYERS = 3
    cfg.MODEL.GENVIS.THRESHOLD = 0.3
    
    cfg.MODEL.SCORE_DECODER = CN()
    cfg.MODEL.SCORE_DECODER.NHEADS = 8
    cfg.MODEL.SCORE_DECODER.DIM_FEEDFORWARD = 2048
    cfg.MODEL.SCORE_DECODER.ENC_LAYERS = 6
    cfg.MODEL.SCORE_DECODER.DEC_LAYERS = 3
    cfg.MODEL.SCORE_DECODER.HIDDEN_DIM = 256
    cfg.MODEL.SCORE_DECODER.TEXT_DIM = 256
    
    cfg.XDECODER = CN()
    cfg.XDECODER.VERBOSE = True
    cfg.XDECODER.MODEL = CN()
    cfg.XDECODER.MODEL.WEIGHTS = 'checkpoints/xdecoder_focalt_last.pt'
    cfg.XDECODER.MODEL.NAME = 'xdecoder_model'
    cfg.XDECODER.MODEL.HEAD = 'xdecoder_head'
    cfg.XDECODER.MODEL.MASK_ON = False
    cfg.XDECODER.MODEL.KEYPOINT_ON = False
    cfg.XDECODER.MODEL.LOAD_PROPOSALS = False
    cfg.XDECODER.MODEL.DIM_PROJ = 512
    cfg.XDECODER.MODEL.BACKBONE_DIM = 768
    cfg.XDECODER.MODEL.TEXT = CN()
    cfg.XDECODER.MODEL.TEXT.ARCH = 'vlpencoder'
    cfg.XDECODER.MODEL.TEXT.NAME = 'transformer'
    cfg.XDECODER.MODEL.TEXT.TOKENIZER = 'clip'
    cfg.XDECODER.MODEL.TEXT.CONTEXT_LENGTH = 77 # 77
    cfg.XDECODER.MODEL.TEXT.WIDTH = 512
    cfg.XDECODER.MODEL.TEXT.HEADS = 8
    cfg.XDECODER.MODEL.TEXT.LAYERS = 12 # 6
    cfg.XDECODER.MODEL.TEXT.AUTOGRESSIVE = True
    
    cfg.XDECODER.MODEL.BACKBONE = CN()
    cfg.XDECODER.MODEL.BACKBONE.NAME = 'focal_dw'
    cfg.XDECODER.MODEL.BACKBONE.PRETRAINED = ''
    cfg.XDECODER.MODEL.BACKBONE.LOAD_PRETRAINED = False
    cfg.XDECODER.MODEL.BACKBONE.FOCAL = CN()
    cfg.XDECODER.MODEL.BACKBONE.FOCAL.PRETRAIN_IMG_SIZE = 224
    cfg.XDECODER.MODEL.BACKBONE.FOCAL.PATCH_SIZE = 4
    cfg.XDECODER.MODEL.BACKBONE.FOCAL.EMBED_DIM = 96
    cfg.XDECODER.MODEL.BACKBONE.FOCAL.DEPTHS = [2, 2, 6, 2]
    cfg.XDECODER.MODEL.BACKBONE.FOCAL.FOCAL_LEVELS = [3, 3, 3, 3]
    cfg.XDECODER.MODEL.BACKBONE.FOCAL.FOCAL_WINDOWS = [3, 3, 3, 3]
    cfg.XDECODER.MODEL.BACKBONE.FOCAL.DROP_PATH_RATE = 0.3
    cfg.XDECODER.MODEL.BACKBONE.FOCAL.MLP_RATIO = 4.0
    cfg.XDECODER.MODEL.BACKBONE.FOCAL.DROP_RATE = 0.0
    cfg.XDECODER.MODEL.BACKBONE.FOCAL.PATCH_NORM = True
    cfg.XDECODER.MODEL.BACKBONE.FOCAL.USE_CONV_EMBED = True
    cfg.XDECODER.MODEL.BACKBONE.FOCAL.SCALING_MODULATOR = True
    cfg.XDECODER.MODEL.BACKBONE.FOCAL.USE_CHECKPOINT = False
    cfg.XDECODER.MODEL.BACKBONE.FOCAL.USE_POSTLN = True
    cfg.XDECODER.MODEL.BACKBONE.FOCAL.USE_POSTLN_IN_MODULATION = False
    cfg.XDECODER.MODEL.BACKBONE.FOCAL.USE_LAYERSCALE = True
    cfg.XDECODER.MODEL.BACKBONE.FOCAL.OUT_FEATURES = ["res2", "res3", "res4", "res5"]
    cfg.XDECODER.MODEL.BACKBONE.FOCAL.OUT_INDICES = [0, 1, 2, 3]
    
    cfg.XDECODER.MODEL.ENCODER = CN()
    cfg.XDECODER.MODEL.ENCODER.NAME = 'transformer_encoder_fpn'
    cfg.XDECODER.MODEL.ENCODER.IGNORE_VALUE = 255
    cfg.XDECODER.MODEL.ENCODER.NUM_CLASSES = 133
    cfg.XDECODER.MODEL.ENCODER.LOSS_WEIGHT = 1.0
    cfg.XDECODER.MODEL.ENCODER.CONVS_DIM = 512
    cfg.XDECODER.MODEL.ENCODER.MASK_DIM = 512
    cfg.XDECODER.MODEL.ENCODER.NORM = "GN"
    cfg.XDECODER.MODEL.ENCODER.IN_FEATURES = ["res2", "res3", "res4", "res5"]
    cfg.XDECODER.MODEL.ENCODER.DEFORMABLE_TRANSFORMER_ENCODER_IN_FEATURES = ["res3", "res4", "res5"]
    cfg.XDECODER.MODEL.ENCODER.COMMON_STRIDE = 4
    cfg.XDECODER.MODEL.ENCODER.TRANSFORMER_ENC_LAYERS = 6

    cfg.XDECODER.MODEL.DECODER = CN()
    cfg.XDECODER.MODEL.DECODER.NAME = 'xdecoder'
    cfg.XDECODER.MODEL.DECODER.TRANSFORMER_IN_FEATURE = 'multi_scale_pixel_decoder'
    cfg.XDECODER.MODEL.DECODER.MASK = True
    cfg.XDECODER.MODEL.DECODER.GROUNDING = CN()
    cfg.XDECODER.MODEL.DECODER.GROUNDING.ENABLED = True
    cfg.XDECODER.MODEL.DECODER.GROUNDING.MAX_LEN = 5
    cfg.XDECODER.MODEL.DECODER.GROUNDING.TEXT_WEIGHT = 2.0
    cfg.XDECODER.MODEL.DECODER.GROUNDING.CLASS_WEIGHT = 0.5
    cfg.XDECODER.MODEL.DECODER.DETECTION = False
    cfg.XDECODER.MODEL.DECODER.CAPTION = CN()
    cfg.XDECODER.MODEL.DECODER.CAPTION.ENABLED = True
    cfg.XDECODER.MODEL.DECODER.CAPTION.PHRASE_PROB = 0.0
    cfg.XDECODER.MODEL.DECODER.CAPTION.SIM_THRES = 0.95
    cfg.XDECODER.MODEL.DECODER.CAPTIONING = CN()
    cfg.XDECODER.MODEL.DECODER.CAPTIONING.ENABLED = True
    cfg.XDECODER.MODEL.DECODER.CAPTIONING.STEP = 50
    cfg.XDECODER.MODEL.DECODER.RETRIEVAL = CN()
    cfg.XDECODER.MODEL.DECODER.RETRIEVAL.ENABLED = True
    cfg.XDECODER.MODEL.DECODER.RETRIEVAL.DIM_IMG = 768
    cfg.XDECODER.MODEL.DECODER.RETRIEVAL.ENSEMBLE = True
    cfg.XDECODER.MODEL.DECODER.DEEP_SUPERVISION = True
    cfg.XDECODER.MODEL.DECODER.NO_OBJECT_WEIGHT = 0.1
    cfg.XDECODER.MODEL.DECODER.CAPTION_WEIGHT = 1.0
    cfg.XDECODER.MODEL.DECODER.CAPTIONING_WEIGHT = 2.0
    cfg.XDECODER.MODEL.DECODER.RETRIEVAL_WEIGHT = 2.0
    cfg.XDECODER.MODEL.DECODER.BACKBONER_WEIGHT = 8.0
    cfg.XDECODER.MODEL.DECODER.GCLASS_WEIGHT = 0.4
    cfg.XDECODER.MODEL.DECODER.GMASK_WEIGHT = 1.0
    cfg.XDECODER.MODEL.DECODER.GDICE_WEIGHT = 1.0
    cfg.XDECODER.MODEL.DECODER.OCLASS_WEIGHT = 0.4
    cfg.XDECODER.MODEL.DECODER.OMASK_WEIGHT = 1.0
    cfg.XDECODER.MODEL.DECODER.ODICE_WEIGHT = 1.0
    cfg.XDECODER.MODEL.DECODER.CLASS_WEIGHT = 2.0
    cfg.XDECODER.MODEL.DECODER.MASK_WEIGHT = 5.0
    cfg.XDECODER.MODEL.DECODER.DICE_WEIGHT = 5.0
    cfg.XDECODER.MODEL.DECODER.BBOX_WEIGHT = 5.0
    cfg.XDECODER.MODEL.DECODER.GIOU_WEIGHT = 2.0
    cfg.XDECODER.MODEL.DECODER.HIDDEN_DIM = 512
    cfg.XDECODER.MODEL.DECODER.NUM_OBJECT_QUERIES = 101
    cfg.XDECODER.MODEL.DECODER.NHEADS = 8
    cfg.XDECODER.MODEL.DECODER.DROPOUT = 0.0
    cfg.XDECODER.MODEL.DECODER.DIM_FEEDFORWARD = 2048
    cfg.XDECODER.MODEL.DECODER.PRE_NORM = False
    cfg.XDECODER.MODEL.DECODER.ENFORCE_INPUT_PROJ = False
    cfg.XDECODER.MODEL.DECODER.SIZE_DIVISIBILITY = 32
    cfg.XDECODER.MODEL.DECODER.TRAIN_NUM_POINTS = 12544
    cfg.XDECODER.MODEL.DECODER.OVERSAMPLE_RATIO = 3.0
    cfg.XDECODER.MODEL.DECODER.IMPORTANCE_SAMPLE_RATIO = 0.75
    cfg.XDECODER.MODEL.DECODER.DEC_LAYERS = 10  # 9 decoder layers, add one for the loss on learnable query
    cfg.XDECODER.MODEL.DECODER.TOP_GROUNDING_LAYERS = 3
    cfg.XDECODER.MODEL.DECODER.TOP_CAPTION_LAYERS = 3
    cfg.XDECODER.MODEL.DECODER.TOP_CAPTIONING_LAYERS = 3
    cfg.XDECODER.MODEL.DECODER.TOP_RETRIEVAL_LAYERS = 3
    cfg.XDECODER.MODEL.DECODER.TEST = CN()
    cfg.XDECODER.MODEL.DECODER.TEST.SEMANTIC_ON = True
    cfg.XDECODER.MODEL.DECODER.TEST.INSTANCE_ON = True
    cfg.XDECODER.MODEL.DECODER.TEST.PANOPTIC_ON = True
    cfg.XDECODER.MODEL.DECODER.TEST.OVERLAP_THRESHOLD = 0.8
    cfg.XDECODER.MODEL.DECODER.TEST.OBJECT_MASK_THRESHOLD = 0.8
    cfg.XDECODER.MODEL.DECODER.TEST.SEM_SEG_POSTPROCESSING_BEFORE_INFERENCE = False

    cfg.XDECODER.DATASETS = CN()
    cfg.XDECODER.DATASETS.TRAIN = ['coco_2017_train_panoptic_filtall_with_sem_seg_caption_grounding', "vlp_train"]
    
    cfg.XDECODER.INPUT = CN()
    cfg.XDECODER.INPUT.PIXEL_MEAN = [123.675, 116.280, 103.530]
    cfg.XDECODER.INPUT.PIXEL_STD = [58.395, 57.120, 57.375]

    cfg.XDECODER.COCO = CN()
    cfg.XDECODER.COCO.TEST = CN()
    cfg.XDECODER.COCO.TEST.DETECTIONS_PER_IMAGE = 100
    cfg.XDECODER.COCO.TEST.NAME = 'coco_eval'
    cfg.XDECODER.COCO.TEST.IOU_TYPE = ['bbox', 'segm']
    cfg.XDECODER.COCO.TEST.USE_MULTISCALE = False
    cfg.XDECODER.COCO.TEST.BATCH_SIZE_TOTAL = 8
    cfg.XDECODER.COCO.TEST.MODEL_FILE = ''
    cfg.XDECODER.COCO.TEST.AUG = CN()
    cfg.XDECODER.COCO.TEST.AUG.ENABLED = False
    cfg.XDECODER.COCO.TRAIN = CN()
    cfg.XDECODER.COCO.TRAIN.ASPECT_RATIO_GROUPING = True
    cfg.XDECODER.COCO.TRAIN.BATCH_SIZE_TOTAL = 2
    cfg.XDECODER.COCO.TRAIN.BATCH_SIZE_PER_GPU = 1
    cfg.XDECODER.COCO.TRAIN.SHUFFLE = True
    cfg.XDECODER.COCO.DATALOADER = CN()
    cfg.XDECODER.COCO.DATALOADER.FILTER_EMPTY_ANNOTATIONS = False
    cfg.XDECODER.COCO.DATALOADER.NUM_WORKERS = 2
    cfg.XDECODER.COCO.DATALOADER.LOAD_PROPOSALS = False
    cfg.XDECODER.COCO.DATALOADER.SAMPLER_TRAIN = "TrainingSampler"
    cfg.XDECODER.COCO.DATALOADER.ASPECT_RATIO_GROUPING = True
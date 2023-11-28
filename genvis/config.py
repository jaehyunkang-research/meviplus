# -*- coding: utf-8 -*-
from detectron2.config import CfgNode as CN


def add_genvis_config(cfg):
    cfg.MODEL.GENVIS = CN()
    cfg.MODEL.GENVIS.LEN_CLIP_WINDOW = 5
    cfg.MODEL.GENVIS.TEXT_HIDDEN_DIM = 768
    cfg.MODEL.GENVIS.FREEZE_TEXT_ENCODER = True
    cfg.MODEL.GENVIS.FUSION_MASK_WEIGHT = 1.0
    cfg.MODEL.GENVIS.FUSION_DICE_WEIGHT = 1.0
    
    cfg.MODEL.TEXT_DECODER = CN()
    cfg.MODEL.TEXT_DECODER.NHEADS = 8
    cfg.MODEL.TEXT_DECODER.DIM_FEEDFORWARD = 2048
    cfg.MODEL.TEXT_DECODER.ENC_LAYERS = 6
    cfg.MODEL.TEXT_DECODER.DEC_LAYERS = 3
    cfg.MODEL.TEXT_DECODER.HIDDEN_DIM = 256
    cfg.MODEL.TEXT_DECODER.TEXT_DIM = 768
    cfg.MODEL.TEXT_DECODER.PROJ_LAYERS = 3
    
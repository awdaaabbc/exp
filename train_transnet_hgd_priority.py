"""Run HGD Model3 training on prioritized subjects by default."""

import argparse
import os

import torch

from train_transnet_hgd import load_config, main


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train Model3 on prioritized HGD subjects.")
    parser.add_argument("--config", default="config/hgd_model3.yaml", help="Path to yaml config.")
    parser.add_argument(
        "--subjects",
        default="10,8,12,13",
        help="Override subjects, for example 10,8,12,13.",
    )
    parser.add_argument("--epochs", type=int, default=None, help="Override training epochs.")
    parser.add_argument("--data-path", default=None, help="Override HGD dataset path.")
    args = parser.parse_args()

    cfg = load_config(args.config)
    cfg["subjects"] = args.subjects
    if args.epochs is not None:
        cfg["epochs"] = args.epochs
    if args.data_path is not None:
        cfg["data_path"] = args.data_path

    os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "max_split_size_mb:128")
    torch.set_num_threads(int(cfg.get("torch_num_threads", 10)))
    main(cfg)

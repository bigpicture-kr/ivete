import os
from dataclasses import dataclass, field

@dataclass
class NLPTrainArguments:
    pretrained_model_name: str = field(
        metadata={"help": "The name of the pretrained model."}
    )
    downstream_task_name: str = field(
        metadata={"help": "The name of the downstream task."}
    )
    downstream_corpus_name: str = field(
        metadata={"help": "The name of the downstream data."}
    )
    downstream_corpus_root_dir: str = field(
        default="./data",
        metadata={"help": "The root directory of the downstream data."}
    )
    downstream_model_dir: str = field(
        default="./checkpoints",
        metadata={"help": "The directory of the output model."}
    )
    max_seq_length: str = field(
        default=128,
        metadata={
            "help": "The maximum total input sequence length after tokenization. Sequences longer "
                    "than this will be truncated, sequences shorter will be padded."
        }
    )
    doc_stride: int = field(
        default=64,
        metadata={
            "help": "When splitting up a long document into chunks, how much stride to take between chunks."
        }
    )
    max_query_length: int = field(
        default=32,
        metadata={
            "help": "The maximum number of tokens for the question. Questions longer than this will "
                    "be truncated to this length."
        }
    )
    threads: int = field(
        default=4,
        metadata={
            "help": "The number of threads, using for preprocessing"
        }
    )
    cpu_workers: int = field(
        default=os.cpu_count(),
        metadata={"help": "The number of CPU workers"}
    )
    save_top_k: int = field(
        default=1,
        metadata={"help": "Save top k model checkpoints."}
    )
    monitor: str = field(
        default="min val_loss",
        metadata={"help": "Monitor condition (save top k)"}
    )
    seed: int = field(
        default=None,
        metadata={"help": "Random seed."}
    )
    overwrite_cache: bool = field(
        default=False,
        metadata={"help": "Overwrite the cached training and evaluation sets"}
    )
    force_download: bool = field(
        default=False,
        metadata={"help": "Force to download downstream data and pretrained models."}
    )
    test_mode: bool = field(
        default=False,
        metadata={"help": "Test Mode enables `fast_dev_run`"}
    )
    learning_rate: float = field(
        default=5e-5,
        metadata={"help": "Learning rate"}
    )
    epochs: int = field(
        default=3,
        metadata={"help": "Max epochs"}
    )
    batch_size: int = field(
        default=32,
        metadata={"help": "Batch size. if 0, Let PyTorch Lightening find the best batch size"}
    )
    fp16: bool = field(
        default=False,
        metadata={"help": "Enable train on FP16"}
    )
    tpu_cores: int = field(
        default=0,
        metadata={"help": "Enable TPU with 1 core or 8 cores"}
    )
    tqdm_enabled: bool = field(
        default=True,
        metadata={"help": "Do tqdnm enabled or not"}
    )

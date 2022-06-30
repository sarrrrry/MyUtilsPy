import random
from typing import Callable

try:
    import numpy as np
except ImportError:
    from myutils.fake import numpy as np
try:
    import torch
except ImportError:
    from myutils.fake import torch as torch


def set_seed(seed: int) -> Callable[[int], None]:
    """
    This is the function to fix random seeds.

    Args:
        seed (int):
    Returns: None
    """

    def worker_init_fn(seed: int):
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)

    worker_init_fn(seed)
    return worker_init_fn

from __future__ import absolute_import

import os
from distutils.version import LooseVersion

import tensorflow.compat.v1 as tf


os.environ["TF_FORCE_GPU_ALLOW_GROWTH"] = "true"

if LooseVersion(tf.__version__) < LooseVersion("2.2.0"):
    raise RuntimeError("DeepXDE requires tensorflow>=2.2.0.")

# Disable TF eager mode
tf.disable_v2_behavior()

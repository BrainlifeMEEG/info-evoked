"""
Print MNE Info summary for evoked data.

This app loads evoked MNE data and writes a text dump of each evoked
condition's `info` structure, also surfacing it in product.json.

Inputs:
    - epo: Path to evoked MNE data (.fif)

Outputs:
    - out_dir/info.txt: Text dump of the evoked info structures
    - product.json: Metadata containing the info summary
"""

# Copyright (c) 2026 brainlife.io
#
# Author: Kami Salibayeva

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'brainlife_utils'))

# Standard imports
import mne

# Import shared utilities
from brainlife_utils import (
    load_config,
    ensure_output_dirs,
    create_product_json,
    add_info_to_product,
    require_config_keys
)

# Ensure output directories exist
ensure_output_dirs('out_dir')

# Load configuration
config = load_config()
require_config_keys(config, ['epo'])

# == LOAD DATA ==
fname = config['epo']
evo = mne.read_evokeds(fname)
# read info from each evoked list element
info = [evo[i].info for i in range(len(evo))]

# == SAVE INFO TEXT FILE ==
with open(os.path.join('out_dir', 'info.txt'), 'w') as f:
    f.write(str(info))

# == CREATE PRODUCT.JSON ==
product_items = []
add_info_to_product(product_items, str(info))
create_product_json(product_items)

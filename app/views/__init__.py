import os
import glob

from trinity.template import Jinja2

# Set TPL (TODO: MOVE TO APP __init__)
tpl = Jinja2(tpls_dir="templates")

# Point all Views to this import
__all__ = [os.path.basename(
    f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]

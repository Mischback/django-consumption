# SPDX-License-Identifier: MIT

"""The app's models.

This is provided as a package instead of a module, because the actual models
are enhanced/augmented with model-related stuff like managers and model forms.
"""

# local imports
from .record import Record  # noqa: F401
from .resource import Resource  # noqa: F401
from .subject import Subject  # noqa: F401

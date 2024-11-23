"""An example plugin style for Pygments."""

from pygments.style import Style
from pygments.token import Keyword

class TitechStyle(Style):
    name = 'titech'
    styles = {
        # This style merely highlights keywords in red.
        Keyword: "#f00",
    }

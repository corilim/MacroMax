import numpy as np

from .. import log
from macromax.utils.array import Grid


def grid2extent(*args):
    """
    Utility function to determine extent values for imshow
    :param args: A Grid object or monotonically increasing ranges, one per dimension (vertical, horizontal)
    :return: a 1D array
    """
    if isinstance(args[0], Grid):
        ranges = args[0]
    else:
        ranges = args
    if len(ranges) > 2:
        log.warning(f"Only using the last two axes in grid2extent(...)!")
    extent = []
    for idx, rng in enumerate(ranges[:-3:-1]):
        rng = np.array(rng).ravel()
        step = rng[1] - rng[0]
        first, last = rng[0] - 0.5 * step, rng[-1] + 0.5 * step
        if idx == 1:
            first, last = last, first
        extent.append(first)
        extent.append(last)

    return np.array(extent)



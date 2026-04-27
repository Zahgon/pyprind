"""
Sebastian Raschka 2014-2017
Python Progress Indicator Utility

Author: Sebastian Raschka <sebastianraschka.com>
License: BSD 3 clause

Contributors: https://github.com/rasbt/pyprind/graphs/contributors
Code Repository: https://github.com/rasbt/pyprind
PyPI: https://pypi.python.org/pypi/PyPrind
"""

from pyprind.prog_class import Prog
import time


class ProgPercent(Prog):
    """
    Initializes a progress bar object that allows visuzalization
    of an iterational computation in the standard output screen.

    Parameters
    ----------
    iterations : `int`
        Number of iterations for the iterative computation.
    track_time : `bool` (default: `True`)
        Prints elapsed time when loop has finished.
    stream : `int` (default: 2).
        Setting the output stream.
        Takes `1` for stdout, `2` for stderr, or a custom stream object
    title : `str` (default: `''`).
        Setting a title for the percentage indicator.
    monitor : `bool` (default: `False`)
        Monitors CPU and memory usage if `True` (requires `psutil` package).
    update_interval : float or int (default: `None`)
        The update_interval in seconds controls how often the progress
        is flushed to the screen.
        Automatic mode if `update_interval=None`.

    """
    def __init__(self, iterations, track_time=True,
                 stream=2, title='', monitor=False, update_interval=None):
        Prog.__init__(self, iterations, track_time, stream,
                      title, monitor, update_interval)
        self.last_progress = 0
        self._print()
        if monitor:
            try:
                self.process.cpu_percent()
                self.process.memory_percent()
            except AttributeError:  # old version of psutil
                self.process.get_cpu_percent()
                self.process.get_memory_percent()

    def _cache_percent_indicator(self, last_progress):
        pass

    def _print(self, force_flush=False):
        """ Prints formatted percentage and tracked time to the screen."""
        pass

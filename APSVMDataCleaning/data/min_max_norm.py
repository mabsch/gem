from __future__ import annotations

import numpy as np
from numba import guvectorize

@guvectorize(['void(float64[:], float64[:], float64[:], float64[:])'], '(n),(),(),(n)')
def min_max_norm(
    w_in: np.ndarray, a_min: float, a_max: float, w_out: np.ndarray
) -> None:
    """Normalize waveform by minimum or maximum value, whichever is
    greater in absolute value.


    Parameters
    ----------
    w_in
        the input waveform
    a_min
        the minimum value
    a_max
        the maximum value
    w_out
        the normalized output waveform

    JSON Configuration Example
    --------------------------

    .. code-block :: json

        "wf_norm": {
            "function": "min_max_norm",
            "module": "pygama.dsp.processors",
            "args": ["wf_blsub", "wf_min", "wf_max", "wf_norm"],
            "unit": ["ADC"]
        }
    """

    if np.isnan(w_in).any():
        return

    w_out[:] = np.nan

    if abs(a_max[0]) == 0 or abs(a_min[0]) == 0:
        w_out[:] = w_in[:]

    elif abs(a_max[0]) >= abs(a_min[0]):
        w_out[:] = w_in[:] / abs(a_max[0])

    elif abs(a_max[0]) < abs(a_min[0]):
        w_out[:] = w_in[:] / abs(a_min[0])
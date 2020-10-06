""" Various Algorithmic Helpers

"""

from ._masking import (
    keep_good_np,
    keep_good_only,
    from_float,
    from_float_np,
    to_f32,
    to_f32_np,
    to_float,
    to_float_np,
    fmask_to_bool,
    enum_to_bool,
    gap_fill,
    choose_first_valid,
)

from ._geomedian import (
    xr_geomedian,
    reshape_for_geomedian,
    int_geomedian,
    int_geomedian_np,
)

from ._dask import (
    chunked_persist,
    chunked_persist_ds,
    chunked_persist_da,
    randomize,
)

from ._rgba import (
    is_rgb,
    to_rgba,
    to_rgba_np,
)

from ._warp import (
    xr_reproject,
)

__all__ = (
    "keep_good_np",
    "keep_good_only",
    "from_float",
    "from_float_np",
    "to_f32",
    "to_f32_np",
    "to_float",
    "to_float_np",
    "fmask_to_bool",
    "enum_to_bool",
    "gap_fill",
    "choose_first_valid",
    "xr_geomedian",
    "int_geomedian",
    "int_geomedian_np",
    "reshape_for_geomedian",
    "chunked_persist",
    "chunked_persist_da",
    "chunked_persist_ds",
    "randomize",
    "is_rgb",
    "to_rgba",
    "to_rgba_np",
    "xr_reproject",
)

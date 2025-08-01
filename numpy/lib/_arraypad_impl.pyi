from typing import (
    Any,
    Literal as L,
    Protocol,
    TypeAlias,
    TypeVar,
    overload,
    type_check_only,
)

from numpy import generic
from numpy._typing import ArrayLike, NDArray, _ArrayLike, _ArrayLikeInt

__all__ = ["pad"]

_ScalarT = TypeVar("_ScalarT", bound=generic)

@type_check_only
class _ModeFunc(Protocol):
    def __call__(
        self,
        vector: NDArray[Any],
        iaxis_pad_width: tuple[int, int],
        iaxis: int,
        kwargs: dict[str, Any],
        /,
    ) -> None: ...

_ModeKind: TypeAlias = L[
    "constant",
    "edge",
    "linear_ramp",
    "maximum",
    "mean",
    "median",
    "minimum",
    "reflect",
    "symmetric",
    "wrap",
    "empty",
]

# TODO: In practice each keyword argument is exclusive to one or more
# specific modes. Consider adding more overloads to express this in the future.

# Expand `**kwargs` into explicit keyword-only arguments
@overload
def pad(
    array: _ArrayLike[_ScalarT],
    pad_width: _ArrayLikeInt,
    mode: _ModeKind = ...,
    *,
    stat_length: _ArrayLikeInt | None = ...,
    constant_values: ArrayLike = ...,
    end_values: ArrayLike = ...,
    reflect_type: L["odd", "even"] = ...,
) -> NDArray[_ScalarT]: ...
@overload
def pad(
    array: ArrayLike,
    pad_width: _ArrayLikeInt,
    mode: _ModeKind = ...,
    *,
    stat_length: _ArrayLikeInt | None = ...,
    constant_values: ArrayLike = ...,
    end_values: ArrayLike = ...,
    reflect_type: L["odd", "even"] = ...,
) -> NDArray[Any]: ...
@overload
def pad(
    array: _ArrayLike[_ScalarT],
    pad_width: _ArrayLikeInt,
    mode: _ModeFunc,
    **kwargs: Any,
) -> NDArray[_ScalarT]: ...
@overload
def pad(
    array: ArrayLike,
    pad_width: _ArrayLikeInt,
    mode: _ModeFunc,
    **kwargs: Any,
) -> NDArray[Any]: ...

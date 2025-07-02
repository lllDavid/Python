import sys
from collections import defaultdict
from types import FrameType
from typing import Any, Callable, Dict, Iterable, Set, Tuple
# Get types at runtime
class Tracer:
    def __init__(self):
        self.var_types: Dict[str, Set[type]] = defaultdict(set)
        self._target_code = None

    def _make_tracer(self, target_code) -> Callable[[FrameType, str, Any], Callable]:
        def tracer(frame: FrameType, event: str, arg: Any):
            if frame.f_code is target_code:
                if event in ('line', 'return'):
                    for name, val in frame.f_locals.items():
                        self.var_types[name].add(type(val))
            return tracer
        return tracer

    def trace(self,
              func: Callable,
              inputs: Iterable[Tuple[Tuple[Any, ...], Dict[str, Any]]]
              ) -> Dict[str, Set[type]]:
        self.var_types.clear()
        self._target_code = func.__code__

        for args, kwargs in inputs:
            tracer = self._make_tracer(self._target_code)
            sys.settrace(tracer)
            try:
                func(*args, **kwargs)
            finally:
                sys.settrace(None)
        return dict(self.var_types)


def sample(a, b):
    x = 42                      # int
    y = 3.14                    # float
    z = "hello"                 # str
    lst = [1, 2, 3]             # list
    dct = {"key": 1}            # dict
    s = {1, 2, 3}               # set
    t = (1, "a", 3.5)           # tuple
    flag = True                 # bool
    none_val = None             # NoneType

    return (a, b, x, y, z, lst, dct, s, t, flag, none_val)


tracer = Tracer()
inputs = [((5, 2), {}), ((1, 10), {})]
result = tracer.trace(sample, inputs)
print(result)
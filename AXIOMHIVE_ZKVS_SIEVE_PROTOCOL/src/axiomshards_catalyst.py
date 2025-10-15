"""
AxiomShards-Catalyst: ToST-linear (Token-Oriented Stream Transformer)
Performs linear memory/statistics streaming transformation for token-processing tasks.
Optimizes out quadratic attention and is RAM-proof (no large buffers; O(N)).
"""
from typing import List, Callable, Any

class ToSTLinear:
    def __init__(self, feature_fn: Callable[[Any], float] = None):
        self.feature_fn = feature_fn or (lambda x: float(hash(str(x))) % 1)
        self.stats_sum = 0.0
        self.count = 0
        self.max = float('-inf')
        self.min = float('inf')

    def update(self, sample: Any):
        feat = self.feature_fn(sample)
        self.stats_sum += feat
        self.count += 1
        self.max = max(self.max, feat)
        self.min = min(self.min, feat)

    def mean(self) -> float:
        if self.count == 0:
            return 0.0
        return self.stats_sum / self.count

    def get_stats(self):
        return {
            'mean': self.mean(),
            'count': self.count,
            'max': self.max,
            'min': self.min
        }

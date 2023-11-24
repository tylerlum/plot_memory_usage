from dataclasses import dataclass
import psutil
import GPUtil
from enum import Enum, auto


class Units(Enum):
    MB = auto()
    GB = auto()
    PERCENT = auto()


@dataclass
class MemoryUsage:
    used_mb: float
    total_mb: float

    @property
    def used_gb(self) -> float:
        return self.used_mb / 1024

    @property
    def total_gb(self) -> float:
        return self.total_mb / 1024

    @property
    def used_percent(self) -> float:
        return self.used_mb / self.total_mb * 100

    @property
    def total_percent(self) -> float:
        return 100

    def get_total(self, units: Units) -> float:
        if units == Units.MB:
            return self.total_mb
        elif units == Units.GB:
            return self.total_gb
        elif units == Units.PERCENT:
            return self.total_percent
        else:
            raise NotImplementedError

    def get_used(self, units: Units) -> float:
        if units == Units.MB:
            return self.used_mb
        elif units == Units.GB:
            return self.used_gb
        elif units == Units.PERCENT:
            return self.used_percent
        else:
            raise NotImplementedError


def get_cpu_memory_usage() -> MemoryUsage:
    return MemoryUsage(
        used_mb=psutil.virtual_memory().used / 1024**2,
        total_mb=psutil.virtual_memory().total / 1024**2,
    )


def get_gpu_memory_usage(device_id: int) -> MemoryUsage:
    return MemoryUsage(
        used_mb=GPUtil.getGPUs()[device_id].memoryUsed,
        total_mb=GPUtil.getGPUs()[device_id].memoryTotal,
    )


def get_num_gpus() -> int:
    return len(GPUtil.getGPUs())

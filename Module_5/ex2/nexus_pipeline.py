#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Protocol, Dict


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Dict:
        print(f"  [InputStage] Validating: {data}")
        if isinstance(data, Dict | str):
            return {}


class TransformStage:
    pass


class OutputStage:
    pass


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()

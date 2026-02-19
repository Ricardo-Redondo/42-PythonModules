#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Protocol


class ProcessingPipeline(ABC):
    pass


class ProcessingStage(Protocol):
    def process(data):
        pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()

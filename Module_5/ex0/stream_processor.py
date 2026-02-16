#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    """Abstract base class for data processors"""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process data and return result description"""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor"""
        pass

    def format_output(self, result: str) -> str:
        """Default formatting for output"""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor for numeric data (lists of numbers)"""

    def process(self, data: Any) -> str:
        """Process numeric data and return statistics"""
        if not self.validate(data):
            return "Invalid data type"
        try:
            count: int = len(data)
            total: float = sum(data)
            avg: float = total / count
            return f"Processed {count} numeric values, sum={total}, avg={avg}"
        except Exception as e:
            return f"Error processing data: {e}"

    def validate(self, data: Any) -> bool:
        """Validate that data is a list of numbers"""
        if not isinstance(data, List[int | float]):
            return False
        for num in data:
            if not isinstance(num, (int, float)):
                return False
        return True


class TextProcessor(DataProcessor):
    """Processor for text data (strings)"""

    def process(self, data: Any) -> str:
        """Process text data and return character and word counts"""
        if not self.validate(data):
            return "Invalid data type"
        char_count: int = len(data)
        word_count: int = len(data.split())
        return f"Processed text: {char_count} characters, {word_count} words"

    def validate(self, data: Any) -> bool:
        """Validate that data is a string"""
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    """Processor for log entries (strings with log levels)"""

    def validate(self, data: Any) -> bool:
        """Validate that data is a string"""
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        """Analyze log entry and detect log level"""
        if not self.validate(data):
            return "Invalid log data"

        if "ERROR" in data:
            level: str = "ERROR"
        elif "WARNING" in data:
            level: str = "WARNING"
        elif "INFO" in data:
            level: str = "INFO"
        else:
            level: str = "UNKNOWN"

        parts: List[str] = data.split(":", 1)
        if len(parts) > 1:
            message: str = parts[1].strip()
        else:
            message: str = data

        return f"[ALERT] {level} level detected: {message}"


def main() -> None:
    """Main function to demonstrate polymorphic processing"""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    num_processor: NumericProcessor = NumericProcessor()
    num_data: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")

    if num_processor.validate(num_data):
        print("Validation: Numeric data verified")
    else:
        print("Validation: failed")

    result: str = num_processor.process(num_data)
    print(num_processor.format_output(result))

    print("\nInitializing Text Processor...")
    text_processor: TextProcessor = TextProcessor()
    text_data: str = "Hello Nexus World"
    print(f"Processing data: \"{text_data}\"")

    if text_processor.validate(text_data):
        print("Validation: Text data verified")
    else:
        print("Validation: failed")

    result: str = text_processor.process(text_data)
    print(text_processor.format_output(result))

    print("\nInitializing Log Processor...")
    log_processor: LogProcessor = LogProcessor()
    log_data: str = "ERROR: Connection timeout"
    print(f"Processing data: \"{log_data}\"")

    if log_processor.validate(log_data):
        print("Validation: Log entry verified")
    else:
        print("Validation: failed")

    result: str = log_processor.process(log_data)
    print(log_processor.format_output(result))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
        ]
    test_data: List[Any] = [[1, 2], "Hello World", "INFO: System ready"]

    for i in range(len(processors)):
        processor: DataProcessor = processors[i]
        data: Any = test_data[i]
        result: str = processor.process(data)
        print(f"Result {i + 1}: {result}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()

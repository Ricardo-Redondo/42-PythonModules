#!/usr/bin/env python3
"""Polymorphic data streaming system for processing mixed data types."""

from abc import ABC, abstractmethod
from typing import List, Any, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class for data streams.

    Provides core streaming functionality with abstract and default methods
    for processing, filtering, and retrieving statistics from data streams.
    """

    def __init__(self) -> None:
        """Initialize the base DataStream."""
        pass

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data.

        Args:
            data_batch: List of data items to process.

        Returns:
            A string describing the processing results.
        """
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria.

        Args:
            data_batch: List of data items to filter.
            criteria: Optional filtering criteria string.

        Returns:
            Filtered list of data items.
        """
        if criteria is None:
            return data_batch
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics.

        Returns:
            Dictionary containing stream statistics.
        """
        return {"stream_id": self.stream_id}


class SensorStream(DataStream):
    """Stream handler for environmental sensor data.

    Processes sensor readings including temperature, humidity,
    and pressure measurements.
    """

    def __init__(self, stream_id: str) -> None:
        """Initialize a SensorStream.

        Args:
            stream_id: Unique identifier for this stream.
        """
        super().__init__()
        self.stream_id: str = stream_id
        self.stream_type: str = "Environmental Data"
        self.read_count: int = 0
        self.temps: List[float] = []

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of sensor readings.

        Args:
            data_batch: List of sensor reading dictionaries.

        Returns:
            Analysis string with reading count and average temperature.
        """
        try:
            for r in data_batch:
                self.read_count += 1
                if isinstance(r, dict) and "temp" in r:
                    self.temps.append(r["temp"])
            av: float = sum(self.temps) / len(self.temps) if self.temps else 0
            c: int = self.read_count
            return f"Sensor analysis: {c} readings processed, avg temp: {av}°C"
        except Exception as e:
            return f"Error processing sensor batch: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter sensor data based on criteria.

        Args:
            data_batch: List of sensor reading dictionaries.
            criteria: Filter type (e.g., "critical" for high readings).

        Returns:
            Filtered list of sensor readings.
        """
        if criteria is None:
            return data_batch
        if criteria == "critical":
            return [r for r in data_batch if isinstance(r, dict) and
                    r.get("humidity", 0) > 50 and r.get("pressure", 0) > 300]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return sensor stream statistics.

        Returns:
            Dictionary with stream_id, type, readings count, and avg temp.
        """
        if self.temps:
            avg_temp: float = sum(self.temps) / len(self.temps)
        else:
            avg_temp: float = 0
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "readings": self.read_count,
            "avg_temp": avg_temp
        }


class TransactionStream(DataStream):
    """Stream handler for financial transaction data.

    Processes buy and sell operations and tracks net flow.
    """

    def __init__(self, stream_id: str) -> None:
        """Initialize a TransactionStream.

        Args:
            stream_id: Unique identifier for this stream.
        """
        super().__init__()
        self.stream_id: str = stream_id
        self.stream_type: str = "Financial Data"
        self.op_count: int = 0
        self.net_flow: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of transactions.

        Args:
            data_batch: List of transaction dictionaries with buy/sell keys.

        Returns:
            Analysis string with operation count and net flow.
        """
        try:
            for o in data_batch:
                self.op_count += 1
                if isinstance(o, dict) and "buy" in o:
                    self.net_flow += o["buy"]
                elif isinstance(o, dict) and "sell" in o:
                    self.net_flow -= o["sell"]
            t: int = self.net_flow
            c: int = self.op_count
            prefix: str = "Transaction analysis:"
            if t <= 0:
                return f"{prefix} {c} operations, net flow: {t} units"
            else:
                return f"{prefix} {c} operations, net flow: +{t} units"
        except Exception as e:
            return f"Error processing transaction batch: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter transactions based on criteria.

        Args:
            data_batch: List of transaction dictionaries.
            criteria: Filter type (filters large transactions > 100).

        Returns:
            Filtered list of transactions.
        """
        if criteria is None:
            return data_batch
        return [t for t in data_batch if isinstance(t, dict) and
                (t.get("buy", 0) > 100 or t.get("sell", 0) > 100)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return transaction stream statistics.

        Returns:
            Dictionary with stream_id, type, operations count, and net flow.
        """
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "operations": self.op_count,
            "net_flow": self.net_flow
        }


class EventStream(DataStream):
    """Stream handler for system event data.

    Processes system events and tracks error occurrences.
    """

    def __init__(self, stream_id: str) -> None:
        """Initialize an EventStream.

        Args:
            stream_id: Unique identifier for this stream.
        """
        super().__init__()
        self.stream_id: str = stream_id
        self.stream_type: str = "System Events"
        self.event_count: int = 0
        self.err_count: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of system events.

        Args:
            data_batch: List of event strings.

        Returns:
            Analysis string with event count and errors detected.
        """
        try:
            for e in data_batch:
                self.event_count += 1
                if isinstance(e, str) and e == "error":
                    self.err_count += 1
            c: int = self.event_count
            err: int = self.err_count
            return f"Event analysis: {c} events, {err} error detected"
        except Exception as ex:
            return f"Error processing event batch: {ex}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter events based on criteria.

        Args:
            data_batch: List of event strings.
            criteria: Filter type (filters for error events).

        Returns:
            Filtered list of events.
        """
        if criteria is None:
            return data_batch
        return [e for e in data_batch if e == "error"]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return event stream statistics.

        Returns:
            Dictionary with stream_id, type, events count, and error count.
        """
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "events": self.event_count,
            "errors": self.err_count
        }


class StreamProcessor:
    """Manages multiple data streams polymorphically.

    Handles adding streams and processing batches across all stream types
    through a unified interface.
    """

    def __init__(self) -> None:
        """Initialize the StreamProcessor with an empty stream list."""
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Add a stream to the processor.

        Args:
            stream: Any DataStream subclass instance.
        """
        self.streams.append(stream)

    def process_all(self, batches: List[Dict[str, List[Any]]]) -> None:
        """Process batches across all registered streams.

        Args:
            batches: List of batch dictionaries mapping stream_id to data.
        """
        for i, batch in enumerate(batches):
            print(f"Batch {i + 1} Results:")
            for stream in self.streams:
                if stream.stream_id in batch:
                    result: str = stream.process_batch(batch[stream.stream_id])
                    short: str = result.split(": ")[1].split(",")[0]

                    if isinstance(stream, SensorStream):
                        print(f"- Sensor data: {short}")
                    elif isinstance(stream, TransactionStream):
                        print(f"- Transaction data: {short}")
                    elif isinstance(stream, EventStream):
                        print(f"- Event data: {short}")


def main() -> None:
    """Demonstrate the polymorphic stream processing system."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor: SensorStream = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    result: str = sensor.process_batch([{"temp": 22.5},
                                        {"humidity": 65},
                                        {"pressure": 1013}])
    print(result + "\n")

    print("Initializing Transaction Stream...")
    trans: TransactionStream = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans.stream_id}, Type: {trans.stream_type}")
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    result = trans.process_batch([{"buy": 100},
                                  {"sell": 150},
                                  {"buy": 75}])
    print(result + "\n")

    print("Initializing Event Stream...")
    event: EventStream = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    print("Processing event batch: [login, error, logout]")
    result = event.process_batch(["login",
                                  "error",
                                  "logout"])
    print(result + "\n")

    processor: StreamProcessor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    batches: List[Dict[str, List[Any]]] = [
        {
            "SENSOR_001": [{"temp": 22.5},
                           {"humidity": 65}],
            "TRANS_001": [{"buy": 100},
                          {"sell": 150},
                          {"buy": 75},
                          {"sell": 50}],
            "EVENT_001": ["login",
                          "error",
                          "logout"]
        }
    ]
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    processor.process_all(batches)

    print("\nStream filtering active: High-priority data only")
    sensor_filtered: List[Any] = sensor.filter_data([
        {"temp": 35, "humidity": 80, "pressure": 500},
        {"temp": 20, "humidity": 40, "pressure": 200}
    ], "critical")
    trans_filtered: List[Any] = trans.filter_data([
        {"buy": 150},
        {"sell": 50},
        {"buy": 200}
    ])
    print(f"Filtered results: {len(sensor_filtered)} critical sensor alerts, "
          f"{len(trans_filtered)} large transactions")

    print("\nAll streams processed successfully. Nexus throughput optimal")


if __name__ == "__main__":
    main()

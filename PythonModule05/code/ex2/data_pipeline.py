from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._next_rank: int = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise ValueError("No data available")
        return self._storage.pop(0)

    def remaining(self) -> int:
        return len(self._storage)

    def get_next_rank(self) -> int:
        return self._next_rank


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for item in data:
                if isinstance(item, bool):
                    return False
                if not isinstance(item, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._storage.append((self._next_rank, str(item)))
                self._next_rank += 1
        else:
            self._storage.append((self._next_rank, str(data)))
            self._next_rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for item in data:
                if isinstance(item, bool):
                    return False
                if not isinstance(item, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._storage.append((self._next_rank, item))
                self._next_rank += 1
        else:
            self._storage.append((self._next_rank, data))
            self._next_rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        def is_valid_dict(d: typing.Any) -> bool:
            if not isinstance(d, dict):
                return False
            for key, value in d.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
            return True

        if is_valid_dict(data):
            return True
        if isinstance(data, list):
            for item in data:
                if not is_valid_dict(item):
                    return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                self._storage.append((self._next_rank, self._format_log(item)))
                self._next_rank += 1
        else:
            self._storage.append((self._next_rank, self._format_log(data)))
            self._next_rank += 1

    def _format_log(self, entry: dict[str, str]) -> str:
        if "log_level" in entry and "log_message" in entry:
            return f"{entry['log_level']}: {entry['log_message']}"
        parts = []
        for key, val in entry.items():
            parts.append(f"{key}: {val}")

        return ", ".join(parts)


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values: list[str] = []
        for _, value in data:
            values.append(value)
        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        parts: list[str] = []
        for rank, value in data:
            escaped_value = value.replace("\\", "\\\\").replace('"', '\\"')
            parts.append(f'"item_{rank}": "{escaped_value}"')
        print("JSON Output:")
        print("{" + ", ".join(parts) + "}")


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(
                    f"DataStream error - "
                    f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self._processors) == 0:
            print("No processor found, no data")
            return
        for proc in self._processors:
            proc_name = type(proc).__name__.replace("Processor", " Processor")
            print(
                f"{proc_name}: total {proc.get_next_rank()}"
                f" items processed, remaining {proc.remaining()} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            exported: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc.remaining() == 0:
                    break
                exported.append(proc.output())
            plugin.process_output(exported)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")

    stream = DataStream()
    stream.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Registering Processors")
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    first_batch: list[typing.Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {first_batch}")
    stream.process_stream(first_batch)
    stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    stream.print_processors_stats()

    second_batch: list[typing.Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"Send another batch of data: {second_batch}")
    stream.process_stream(second_batch)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    main()

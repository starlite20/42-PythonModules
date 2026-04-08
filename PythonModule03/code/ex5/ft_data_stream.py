import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["bob", "alice", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "climb", "release", "swim"]

    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
        events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        yield events.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    generator = gen_event()

    for i in range(1000):
        event = next(generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    generator = gen_event()
    event_list = []

    for _ in range(10):
        event_list.append(next(generator))

    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()

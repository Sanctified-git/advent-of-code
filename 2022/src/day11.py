from dataclasses import dataclass
from typing import Callable
from utils.io import get_input


@dataclass
class Monkey:
    items: list[int]
    operation: Callable[[int], int]
    divisor: int
    targets: list
    relief: bool
    inspected: int = 0
    common_divisor: int = 1

    def throw_item(self, item) -> int:
        if not item % self.divisor:
            monkeys[self.targets[0]].catch_item(item)
        else:
            monkeys[self.targets[1]].catch_item(item)

    def catch_item(self, item: int):
        self.items.append(item)

    def worry_human(self) -> None:
        for i in self.items:
            i = self.operation(i)

            if self.relief:
                i //= 3
            elif i > Monkey.common_divisor:
                i %= Monkey.common_divisor

            self.inspected += 1
            self.throw_item(i)
        self.items.clear()


def day11(rounds: int, relief: bool = True):
    """https://adventofcode.com/2022/day/11"""
    global monkeys
    input: list = get_input(__file__)

    ### INITIALIZE MONKEYS ###

    monkeys = []
    items: list[int] = []
    operation: str
    divisor: int
    targets: list = []
    Monkey.common_divisor = 1

    iterator = iter(range(len(input)))
    for i in iterator:
        if not input[i]:
            continue
        args = input[i].strip().split(" ")
        if args[0] == "Starting":
            items = [int(i.rstrip(",")) for i in args[2:]]
        elif args[0] == "Operation:":
            operation = eval("lambda old: " + " ".join(args[-3:]))
        elif args[0] == "Test:":
            divisor = int(args.pop())
            Monkey.common_divisor *= divisor
        elif args[1] == "true:":
            targets.append(int(args.pop()))
        elif args[1] == "false:":
            targets.append(int(args.pop()))
            monkeys.append(Monkey(items, operation, divisor, targets, relief))
            targets = []

    ### PLAY OUT TURNS ###

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.worry_human()

    inspected: list = [m.inspected for m in monkeys]
    inspected.sort(reverse=True)

    print(f" The level of monkey business after {rounds} rounds is {inspected[0] * inspected[1]}")


if __name__ == "__main__":
    monkeys: list[Monkey]
    day11(20)  # PART ONE
    day11(10000, False)  # PART TWO

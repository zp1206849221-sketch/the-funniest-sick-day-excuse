"""Write the funniest sick-day excuse to /output/entry.txt."""

import os

LINE = (
    "Morning \u2014 can't come in, the gas-station tuna roll I defended as "
    "'probably fine' at 1 a.m. has won the argument, and my stomach is now "
    "presenting its evidence hourly."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
r"""Expand line-level LaTeX \input directives into one submission source."""

import argparse
import re
from pathlib import Path


INPUT_RE = re.compile(r"^(?P<indent>\s*)\\input\{(?P<name>[^}]+)\}\s*$")


def expand(path: Path, stack: tuple[Path, ...] = ()) -> str:
    path = path.resolve()
    if path in stack:
        chain = " -> ".join(str(item) for item in (*stack, path))
        raise RuntimeError(f"cyclic input: {chain}")

    output = []
    for line in path.read_text(encoding="utf-8").splitlines(keepends=True):
        match = INPUT_RE.match(line.rstrip("\n"))
        if not match:
            output.append(line)
            continue

        input_name = match.group("name")
        child = Path(input_name)
        if child.suffix == "":
            child = child.with_suffix(".tex")
        child = path.parent / child
        output.append(f"% BEGIN expanded input: {input_name}\n")
        output.append(expand(child, (*stack, path)))
        output.append(f"% END expanded input: {input_name}\n")
    return "".join(output)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.write_text(expand(args.source), encoding="utf-8")


if __name__ == "__main__":
    main()

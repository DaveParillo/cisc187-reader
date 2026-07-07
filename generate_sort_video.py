#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


SORTS = ("bubble", "selection", "insertion", "shell", "merge", "quick", "heap")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate prebuilt sort animation WebM videos and PNG thumbnails."
    )
    parser.add_argument(
        "sorts",
        nargs="*",
        choices=SORTS,
        default=SORTS,
        help="Sort animations to generate. Defaults to all sorts.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("src/_static/generated/sort"),
        help="Directory for generated WebM and PNG assets.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent
    cache_root = repo_root / "build" / "sort-animation-cache"
    matplotlib_cache = cache_root / "matplotlib"
    xdg_cache = cache_root / "xdg"
    matplotlib_cache.mkdir(parents=True, exist_ok=True)
    xdg_cache.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("MPLCONFIGDIR", str(matplotlib_cache))
    os.environ.setdefault("XDG_CACHE_HOME", str(xdg_cache))
    os.environ.setdefault("MPLBACKEND", "Agg")

    sort_module_dir = repo_root / "src" / "sort"
    sys.path.insert(0, str(sort_module_dir))

    os.environ["SORT_ANIMATION_OUTPUT_DIR"] = str((repo_root / args.output_dir).resolve())

    from sort_animation_assets import generate_sort_assets

    for sort_name in args.sorts:
        print(f"Generating {sort_name} sort assets...")
        generate_sort_assets(sort_name)

    print(f"Generated assets in {os.environ['SORT_ANIMATION_OUTPUT_DIR']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import random
import sys
import os
from collections.abc import Callable, Iterable
from pathlib import Path

import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import rcParams


BAR_COLOR = "#3498db"
COMPARE_COLOR = "#e74c3c"
CURRENT_COLOR = "#f1c40f"
MARK_COLOR = "#8e44ad"
BOUNDARY_COLOR = "#1abc9c"
SORTED_COLOR = "#95a5a6"
BACKGROUND = "#ffffff"
FPS = 4
FINAL_HOLD_SECONDS = 1.25

Frame = tuple[list[int], dict[int, str], str]
FrameBuilder = Callable[[list[int]], list[Frame]]


def case_inputs(size: int = 18) -> dict[str, tuple[str, list[int]]]:
    best = list(range(1, size + 1))
    worst = list(range(size, 0, -1))
    average = best.copy()
    random.Random(187).shuffle(average)
    return {
        "average": ("Average case", average),
        "best": ("Best case", best),
        "worst": ("Worst case", worst),
    }


def sorted_colors(start: int, stop: int, color: str = SORTED_COLOR) -> dict[int, str]:
    return {index: color for index in range(start, stop)}


def add_final_hold(frames: list[Frame]) -> list[Frame]:
    hold_count = max(1, int(FPS * FINAL_HOLD_SECONDS))
    return [*frames, *([frames[-1]] * hold_count)]


def bubble_frames(values: list[int]) -> list[Frame]:
    data = values.copy()
    frames: list[Frame] = [(data.copy(), {}, "Initial")]
    n = len(data)

    for pass_index in range(n - 1):
        swapped = False
        sorted_start = n - pass_index
        for index in range(0, n - pass_index - 1):
            colors = sorted_colors(sorted_start, n)
            colors[index] = COMPARE_COLOR
            colors[index + 1] = COMPARE_COLOR
            if data[index] > data[index + 1]:
                data[index], data[index + 1] = data[index + 1], data[index]
                swapped = True
            frames.append((data.copy(), colors, f"Compare positions {index} and {index + 1}"))
        if not swapped:
            break

    frames.append((data.copy(), sorted_colors(0, n), "Sorted"))
    return frames


def selection_frames(values: list[int]) -> list[Frame]:
    data = values.copy()
    frames: list[Frame] = [(data.copy(), {}, "Initial")]
    n = len(data)

    for slot in range(n - 1, 0, -1):
        largest = 0
        for location in range(1, slot + 1):
            colors = sorted_colors(slot + 1, n)
            colors[slot] = BOUNDARY_COLOR
            colors[largest] = CURRENT_COLOR
            colors[location] = COMPARE_COLOR
            frames.append((data.copy(), colors, "Find largest remaining value"))
            if data[location] > data[largest]:
                largest = location
        data[slot], data[largest] = data[largest], data[slot]
        colors = sorted_colors(slot, n)
        colors[largest] = COMPARE_COLOR
        frames.append((data.copy(), colors, "Place largest value"))

    frames.append((data.copy(), sorted_colors(0, n), "Sorted"))
    return frames


def insertion_frames(values: list[int]) -> list[Frame]:
    data = values.copy()
    frames: list[Frame] = [(data.copy(), {0: SORTED_COLOR}, "Initial sorted prefix")]
    n = len(data)

    for index in range(1, n):
        current = data[index]
        position = index
        colors = sorted_colors(0, index)
        colors[index] = CURRENT_COLOR
        frames.append((data.copy(), colors, "Choose next value"))
        while position > 0 and data[position - 1] > current:
            data[position] = data[position - 1]
            colors = sorted_colors(0, index + 1)
            colors[position - 1] = COMPARE_COLOR
            colors[position] = CURRENT_COLOR
            frames.append((data.copy(), colors, "Shift larger value right"))
            position -= 1
        data[position] = current
        colors = sorted_colors(0, index + 1)
        colors[position] = CURRENT_COLOR
        frames.append((data.copy(), colors, "Insert value"))

    frames.append((data.copy(), sorted_colors(0, n), "Sorted"))
    return frames


def shell_frames(values: list[int]) -> list[Frame]:
    data = values.copy()
    frames: list[Frame] = [(data.copy(), {}, "Initial")]
    n = len(data)
    gap = n // 2

    while gap > 0:
        for start in range(gap):
            for index in range(start + gap, n, gap):
                current = data[index]
                position = index
                colors = {i: BOUNDARY_COLOR for i in range(start, n, gap)}
                colors[index] = CURRENT_COLOR
                frames.append((data.copy(), colors, f"Gap {gap}: choose value"))
                while position >= gap and data[position - gap] > current:
                    data[position] = data[position - gap]
                    colors = {i: BOUNDARY_COLOR for i in range(start, n, gap)}
                    colors[position - gap] = COMPARE_COLOR
                    colors[position] = CURRENT_COLOR
                    frames.append((data.copy(), colors, f"Gap {gap}: shift value"))
                    position -= gap
                data[position] = current
                colors = {i: BOUNDARY_COLOR for i in range(start, n, gap)}
                colors[position] = CURRENT_COLOR
                frames.append((data.copy(), colors, f"Gap {gap}: insert value"))
        gap //= 2

    frames.append((data.copy(), sorted_colors(0, n), "Sorted"))
    return frames


def merge_frames(values: list[int]) -> list[Frame]:
    data = values.copy()
    frames: list[Frame] = [(data.copy(), {}, "Initial")]
    n = len(data)

    def merge_sort(start: int, stop: int) -> None:
        if stop - start <= 1:
            return
        mid = (start + stop) // 2
        frames.append((data.copy(), {i: MARK_COLOR for i in range(start, stop)}, "Split range"))
        merge_sort(start, mid)
        merge_sort(mid, stop)

        left = data[start:mid]
        right = data[mid:stop]
        i = j = 0
        target = start
        while i < len(left) and j < len(right):
            colors = {k: BOUNDARY_COLOR for k in range(start, stop)}
            colors[target] = CURRENT_COLOR
            if left[i] <= right[j]:
                data[target] = left[i]
                i += 1
            else:
                data[target] = right[j]
                j += 1
            frames.append((data.copy(), colors, "Merge smallest value"))
            target += 1
        for remaining in left[i:]:
            data[target] = remaining
            frames.append((data.copy(), {target: CURRENT_COLOR}, "Copy remaining left value"))
            target += 1
        for remaining in right[j:]:
            data[target] = remaining
            frames.append((data.copy(), {target: CURRENT_COLOR}, "Copy remaining right value"))
            target += 1
        frames.append((data.copy(), {k: SORTED_COLOR for k in range(start, stop)}, "Merged range"))

    merge_sort(0, n)
    frames.append((data.copy(), sorted_colors(0, n), "Sorted"))
    return frames


def quick_frames(values: list[int]) -> list[Frame]:
    data = values.copy()
    frames: list[Frame] = [(data.copy(), {}, "Initial")]
    n = len(data)
    sorted_positions: set[int] = set()

    def partition(first: int, last: int) -> int:
        pivot = data[first]
        left = first + 1
        right = last - 1
        while True:
            while left <= right and data[left] <= pivot:
                colors = {i: SORTED_COLOR for i in sorted_positions}
                colors[first] = CURRENT_COLOR
                colors[left] = COMPARE_COLOR
                colors[right] = BOUNDARY_COLOR
                frames.append((data.copy(), colors, "Scan from left"))
                left += 1
            while right >= left and data[right] >= pivot:
                colors = {i: SORTED_COLOR for i in sorted_positions}
                colors[first] = CURRENT_COLOR
                if left < last:
                    colors[left] = BOUNDARY_COLOR
                colors[right] = COMPARE_COLOR
                frames.append((data.copy(), colors, "Scan from right"))
                right -= 1
            if right < left:
                break
            data[left], data[right] = data[right], data[left]
            colors = {i: SORTED_COLOR for i in sorted_positions}
            colors[first] = CURRENT_COLOR
            colors[left] = COMPARE_COLOR
            colors[right] = COMPARE_COLOR
            frames.append((data.copy(), colors, "Swap around pivot"))

        data[first], data[right] = data[right], data[first]
        sorted_positions.add(right)
        colors = {i: SORTED_COLOR for i in sorted_positions}
        colors[right] = CURRENT_COLOR
        frames.append((data.copy(), colors, "Place pivot"))
        return right

    def quick_sort(first: int, last: int) -> None:
        if last - first <= 1:
            if first < last:
                sorted_positions.add(first)
            return
        pivot_index = partition(first, last)
        quick_sort(first, pivot_index)
        quick_sort(pivot_index + 1, last)

    quick_sort(0, n)
    frames.append((data.copy(), sorted_colors(0, n), "Sorted"))
    return frames


def heap_frames(values: list[int]) -> list[Frame]:
    data = values.copy()
    frames: list[Frame] = [(data.copy(), {}, "Initial")]
    n = len(data)

    def boundary_colors(heap_size: int) -> dict[int, str]:
        colors = sorted_colors(heap_size, n)
        if heap_size < n:
            colors[heap_size] = BOUNDARY_COLOR
        return colors

    def sift_down(start: int, heap_size: int, label: str) -> None:
        root = start
        while True:
            child = 2 * root + 1
            if child >= heap_size:
                break
            swap = root
            colors = boundary_colors(heap_size)
            colors[root] = CURRENT_COLOR
            colors[child] = COMPARE_COLOR
            if child + 1 < heap_size:
                colors[child + 1] = COMPARE_COLOR
            frames.append((data.copy(), colors, label))

            if data[swap] < data[child]:
                swap = child
            if child + 1 < heap_size and data[swap] < data[child + 1]:
                swap = child + 1
            if swap == root:
                return

            data[root], data[swap] = data[swap], data[root]
            colors = boundary_colors(heap_size)
            colors[root] = COMPARE_COLOR
            colors[swap] = COMPARE_COLOR
            frames.append((data.copy(), colors, "Move larger child up"))
            root = swap

    for start in range(n // 2 - 1, -1, -1):
        colors = boundary_colors(n)
        colors[start] = CURRENT_COLOR
        frames.append((data.copy(), colors, "Build max heap"))
        sift_down(start, n, "Heapify subtree")

    frames.append((data.copy(), {index: MARK_COLOR for index in range(n)}, "Max heap built"))

    for end in range(n - 1, 0, -1):
        data[0], data[end] = data[end], data[0]
        colors = boundary_colors(end)
        colors[0] = COMPARE_COLOR
        colors[end] = CURRENT_COLOR
        frames.append((data.copy(), colors, "Move max value to sorted suffix"))
        sift_down(0, end, "Restore heap")

    frames.append((data.copy(), sorted_colors(0, n), "Sorted"))
    return frames


BUILDERS: dict[str, tuple[str, FrameBuilder]] = {
    "bubble": ("Bubble sort", bubble_frames),
    "selection": ("Selection sort", selection_frames),
    "insertion": ("Insertion sort", insertion_frames),
    "shell": ("Shell sort", shell_frames),
    "merge": ("Merge sort", merge_frames),
    "quick": ("Quick sort", quick_frames),
    "heap": ("Heap sort", heap_frames),
}


def draw_frame(ax, values: list[int], colors: dict[int, str], title: str) -> None:
    ax.clear()
    ax.set_facecolor(BACKGROUND)
    ax.set_title(title, fontsize=11)
    ax.set_xlim(-0.2, len(values))
    ax.set_ylim(0, max(values) + 2)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    bar_colors = [colors.get(index, BAR_COLOR) for index in range(len(values))]
    ax.bar(range(len(values)), values, align="edge", color=bar_colors, width=0.88)


def configure_ffmpeg() -> None:
    try:
        import imageio_ffmpeg
    except ImportError:
        return
    rcParams["animation.ffmpeg_path"] = imageio_ffmpeg.get_ffmpeg_exe()


def save_video(values: list[int], output_path: Path, title: str, builder: FrameBuilder) -> None:
    configure_ffmpeg()
    if not animation.writers.is_available("ffmpeg"):
        raise RuntimeError(
            "WebM output requires ffmpeg or the imageio-ffmpeg Python package. "
            "Install imageio-ffmpeg in the build environment to generate sort video assets."
        )

    frames = add_final_hold(builder(values))
    fig, ax = plt.subplots(figsize=(6, 3.5), dpi=110)
    fig.patch.set_facecolor(BACKGROUND)

    def update(frame: Frame):
        data, colors, label = frame
        draw_frame(ax, data, colors, f"{title}: {label}")
        return ax.patches

    anim = animation.FuncAnimation(
        fig,
        update,
        frames=frames,
        interval=1000 / FPS,
        repeat=True,
        repeat_delay=1200,
        cache_frame_data=False,
    )
    writer = animation.FFMpegWriter(
        fps=FPS,
        codec="libvpx-vp9",
        extra_args=["-pix_fmt", "yuv420p", "-b:v", "0", "-crf", "35"],
    )
    anim.save(output_path, writer=writer)
    plt.close(fig)


def summary_indices(count: int) -> Iterable[int]:
    return [0, max(0, count // 2), count - 1]


def save_summary(values: list[int], output_path: Path, title: str, builder: FrameBuilder) -> None:
    frames = builder(values)
    subtitles = ["Initial", "Midway", "Sorted"]

    fig, axes = plt.subplots(1, 3, figsize=(9, 3.2), dpi=120)
    fig.patch.set_facecolor(BACKGROUND)
    fig.suptitle(title, fontsize=14)
    for ax, frame_index, subtitle in zip(axes, summary_indices(len(frames)), subtitles):
        data, colors, _ = frames[frame_index]
        if subtitle == "Sorted":
            colors = sorted_colors(0, len(data))
        draw_frame(ax, data, colors, subtitle)
    fig.tight_layout()
    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


def output_dir() -> Path:
    if output := os.environ.get("SORT_ANIMATION_OUTPUT_DIR"):
        generated = Path(output).resolve()
        generated.mkdir(parents=True, exist_ok=True)
        return generated
    source_path = Path(sys.argv[0]).resolve()
    generated = source_path.parents[1] / "_static" / "generated" / "sort"
    generated.mkdir(parents=True, exist_ok=True)
    return generated


def generate_sort_assets(sort_name: str) -> None:
    display_name, builder = BUILDERS[sort_name]
    out = output_dir()
    for slug, (case_label, values) in case_inputs().items():
        title = f"{display_name} - {case_label}"
        prefix = f"{sort_name}-sort-{slug}"
        save_video(values, out / f"{prefix}.webm", title, builder)
        save_summary(values, out / f"{prefix}.png", title, builder)

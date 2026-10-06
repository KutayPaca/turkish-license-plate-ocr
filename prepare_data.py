from __future__ import annotations

import argparse
import random
from pathlib import Path


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg"}


def write_list(
    image_names: list[str], image_dir: Path, output_file: Path
) -> None:
    with output_file.open("w", encoding="utf-8") as file:
        for image_name in image_names:
            label = Path(image_name).stem.replace("-", " ")
            image_path = (image_dir / image_name).as_posix()
            file.write(f"{image_path}\t{label}\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create PaddleOCR train and validation label files."
    )
    parser.add_argument(
        "--image-dir",
        type=Path,
        default=Path("dataset/plakalar/license-plates"),
        help="Directory containing plate images.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("."),
        help="Directory for train_list.txt and val_list.txt.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=20_000,
        help="Maximum number of images to include.",
    )
    args = parser.parse_args()

    image_dir = args.image_dir.resolve()
    if not image_dir.is_dir():
        raise FileNotFoundError(f"Image directory not found: {image_dir}")
    if args.limit <= 0:
        raise ValueError("--limit must be greater than zero.")

    image_names = sorted(
        path.name
        for path in image_dir.iterdir()
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
    )
    random.Random(42).shuffle(image_names)
    selected_images = image_names[: args.limit]

    split_index = int(len(selected_images) * 0.8)
    train_images = selected_images[:split_index]
    val_images = selected_images[split_index:]

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    write_list(train_images, image_dir, output_dir / "train_list.txt")
    write_list(val_images, image_dir, output_dir / "val_list.txt")

    print(f"Found {len(image_names)} images.")
    print(f"Created {len(train_images)} training and {len(val_images)} validation labels.")


if __name__ == "__main__":
    main()

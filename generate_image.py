import json
from pathlib import Path

IMAGE_FOLDER = Path("images")
OUTPUT_FILE = IMAGE_FOLDER / "images.json"

allowed_extensions = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".gif"
}

images = sorted(
    [
        file.name
        for file in IMAGE_FOLDER.iterdir()
        if file.is_file()
        and file.suffix.lower() in allowed_extensions
    ]
)

OUTPUT_FILE.write_text(
    json.dumps(images, indent=2),
    encoding="utf-8"
)

print(f"Found {len(images)} images.")
print(f"Created: {OUTPUT_FILE}")

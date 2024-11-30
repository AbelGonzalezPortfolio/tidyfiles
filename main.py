from pathlib import Path

import filetype

import PIL.Image
import random
import string

# Define Input folder path
# INPUT_PATH = Path("/media/abel/Archive SSD/hd-rec-8/part6")
INPUT_PATH = Path("/media/abel/Portable-SSD/hd-5/raw")


# Define output folder path
# OUTPUT_PATH = Path("/media/abel/Archive SSD/hd-rec-8/output")
OUTPUT_PATH = Path("/media/abel/Portable-SSD/hd-5/output")


# iterate through each file in the input path
def yield_files(path):
    for file in path.glob("**/*"):
        if file.is_file():
            yield file


# get type of file
# move to output folder inside a new folder named after the file type
def get_image_info(file):
    try:
        image = PIL.Image.open(file)
    except Exception as e:
        return None
        print("Error reading image")
    exif = image.getexif()
    image_info = {}
    image_info["resolution"] = image.size[0] * image.size[1]

    if 271 in exif:
        image_info["camera_make"] = exif[271]
        if 272 in exif:
            image_info["camera_model"] = exif[272]

    return image_info


def find_and_move(path):
    stats = {"moved": 0, "not_moved": 0, "attempted": 0}

    # Iterate through files including subfolders in input
    for file in yield_files(INPUT_PATH):
        # Read filetype
        kind = filetype.guess(file)

        # Update stats
        stats["attempted"] += 1

        # Skip if not identified
        if kind is None:
            stats["not_moved"] += 1
            continue

        output_file = OUTPUT_PATH / kind.mime

        # If image set a different path
        if kind.mime.split("/")[0] == "image":
            try:
                image_info = get_image_info(file)
            except Exception as e:
                continue
            if image_info is not None:
                if "camera_make" in image_info:
                    output_file = output_file / image_info["camera_make"]
                    if "camera_model" in image_info:
                        output_file = output_file / image_info["camera_model"]
                    else:
                        output_file = output_file / "no_model"
                else:
                    output_file = output_file / "no_exif"
                    if image_info["resolution"] < 50000:
                        output_file = output_file / "lo-res"
                    elif (
                        image_info["resolution"] > 50000
                        and image_info["resolution"] < 250000
                    ):
                        output_file = output_file / "mid-res"
                    else:
                        output_file = output_file / "hi-res"

        output_file = Path(str(output_file).replace("\x00", ""))
        output_file.mkdir(parents=True, exist_ok=True)

        if not file.suffix:
            new_filename = f"{file.name}.{kind.extension}"
        else:
            new_filename = file.name

        new_file_path = output_file / new_filename
        while new_file_path.exists():
            letters_and_digits = string.ascii_uppercase + string.digits
            file_name_split = new_filename.split(".")
            new_filename = (
                file_name_split[0]
                + random.choice(letters_and_digits)
                + "."
                + file_name_split[-1]
            )
            new_file_path = output_file / new_filename

            print("warning - file already exists")
            print(f"renaming to - {new_filename}")

        file.rename(new_file_path)
        stats["moved"] += 1

        print(
            f"Attempted: {stats['attempted']}, Moved: {stats['moved']}, Not Moved: {stats['not_moved']}",
            end="\r",
        )

    # print(
    #     f"============================================\nExtraction Completed\nMoved: {moved_count} files\nNot Moved: {not_moved_count} files\n============================================",
    # )
    # print(file.suffix)
    # print(kind.mime)


find_and_move(INPUT_PATH)

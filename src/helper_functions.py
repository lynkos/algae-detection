from os import remove, listdir, mkdir, curdir
from os.path import splitext, basename, isdir, exists, abspath
from hashlib import sha1
from random import sample
from PIL.Image import open as open_img
from pathlib import Path
from re import search

DIRECTORY = Path(abspath(curdir), "dataset", "orig_data")
"""Directory containing images, each of which are in their respective subdirectories"""

OVERREPRESENTED = ["non-algae", "oscillatoria"]
"""List of categories that are overrepresented in the dataset"""

UNDERREPRESENTED = ["closterium", "microcystis", "nitzschia"]
"""List of categories that are underrepresented (i.e., not overrepresented) in the dataset"""

SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".bmp", ".webm")
"""Image formats currently supported by RoboFlow"""

def is_valid_img(img_path: Path) -> bool:
    """
    Checks if image at filepath is a valid image

    Args:
        img_path (Path): Path to image file

    Returns:
        bool: True if image is valid, else False
    """
    return img_path.is_file() and (img_path.suffix.lower() in SUPPORTED_FORMATS)

def count_files(directory: Path) -> int:
    """
    Counts how many valid files are in a given directory

    Args:
        directory (Path): Path to directory containing images

    Returns:
        int: Number of files within directory
    """
    return sum(1 for file in directory.rglob("*") if is_valid_img(file))

def crop_img(img_path: Path) -> None:
    """
    Crops image at filepath so it has a width : height ratio of 4 : 3
    
    Image size = (orig_width, orig_length)
    Desired size = (width, length)
    New dimensions = (orig_width - width) / 2, (orig_length - length) / 2, (orig_width + width) / 2, (orig_length + length) / 2

    Args:
        img_path (Path): Path to image file
    """
    img = open_img(img_path)
    orig_width, orig_length = img.size
    length = (orig_width * 3) / 4
    img.crop((0, int((orig_length - length) / 2), orig_width, int((orig_length + length) / 2))).save(img_path)

def standardize(category_path: Path) -> None:
    """
    Removes duplicate and near duplicate images in category and crops all images in
    category so they all have the same width : height ratio (i.e., 4 : 3)

    Args:
        category_path (Path): Path to category directory
    """
    hashes = set()

    for img in listdir(category_path):
        img_path = Path(category_path / img)

        if is_valid_img(img_path):
            digest = sha1(open(img_path, "rb").read()).digest()

            if search(r"\(\d+\)", splitext(basename(img))[0]):
                print(f"Removing {img_path} because its name implies it's a duplicate")
                remove(img_path)
        
            elif digest not in hashes:
                print(f"Retaining and cropping {img_path} since it's not a duplicate")
                hashes.add(digest)
                #crop_img(img_path)
                
            else:
                print(f"Removing {img_path} because it's a near duplicate")
                remove(img_path)
    
def choose_random_imgs(category: Path, num_samples: int) -> None:
    """
    Chooses random subset of images from overrepresented categories
    and moves them to new subdirectory 

    Args:
        category (Path): Directory path of category
        num_samples (int): Number of samples to randomly choose
    """
    new_path = Path(category / "selected_samples")

    if not exists(new_path): mkdir(new_path)
    
    for img in sample(listdir(category), num_samples):
        img_path = Path(category / img)
        
        if is_valid_img(img_path):
            Path(img_path).rename(new_path / img)
            print(f"Moved {img} to {new_path}")
            
def cleanup(directory: Path = DIRECTORY) -> None:
    """
    1. Remove duplicates and near duplicates
    2. Standardize images so they all have the same width : height ratio (i.e., 4 : 3)
    3. Choose random subset of images from overrepresented directories and move
       them to new subdirectory

    Args:
        directory (Path, optional): Directory containing categories; defaults to DIRECTORY
    """
    total = 0
    
    for under_category in UNDERREPRESENTED:
        under_path = Path(directory / under_category)
        
        if isdir(under_path):
            standardize(under_path)
            total += count_files(under_path)

    avg_under_count = total // len(UNDERREPRESENTED)
    
    for over_category in OVERREPRESENTED:
        over_path = Path(directory / over_category)

        if isdir(over_path):
            standardize(over_path)
            choose_random_imgs(over_path, avg_under_count)

def get_image_shapes(directory: Path = DIRECTORY) -> dict[tuple[int, int], int]:
    """
    Get dimensions and frequency of images within in a given directory's subdirectories

    Args:
        directory (Path, optional): Directory containing categories; defaults to DIRECTORY

    Returns:
        dict[tuple[int, int], int]: Dictionary containing unique image shapes in dataset and how often they occur
    """
    shape_and_occurrence = dict()
    
    for folder_name in listdir(directory):
        subdirectory = Path(directory / folder_name)
        
        if isdir(subdirectory):
            for file in listdir(subdirectory):
                file_path = Path(subdirectory / file)
                
                if is_valid_img(file_path):
                    shape = open_img(file_path).size
                    
                    if shape not in shape_and_occurrence: shape_and_occurrence[shape] = 1

                    elif shape in shape_and_occurrence:
                        count = shape_and_occurrence[shape]
                        count += 1
                        shape_and_occurrence[shape] = count

    return shape_and_occurrence

if "__main__" == __name__:
    print(get_image_shapes())
from crimson.file_loader.utils import (
    filter_paths as _filter_paths,
    )
from pathlib import Path
import zipfile


def create_zip_from_dir(
    input_dir: str,
    output_dir: str,
    zip_name: str = "test.zip",
    includes=[
        ".py"
    ],
    excludes=[
        ".pytest_cache",
        "__pycache__,"    
    ]) -> str:
    paths = _filter_paths(input_dir, includes, excludes)
    output_path = Path(output_dir).resolve()

    output_path.mkdir(parents=True, exist_ok=True)

    zip_path = output_path / zip_name

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for path in paths:
            zipf.write(path, arcname=Path(path).name)

    return str(zip_path)


def extract_zip_to_dir(zip_path: str, output_dir: str="./test") -> str:
    zip_file = Path(zip_path).resolve()
    output_path = Path(output_dir).resolve()

    output_path.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(output_path)

    return str(output_path)

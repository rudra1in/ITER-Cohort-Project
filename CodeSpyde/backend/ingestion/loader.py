import json
from pathlib import Path


SUPPORTED_EXTENSIONS = {
    ".json",
    ".md",
    ".markdown",
    ".txt"
}


def discover_files(
    directory: str | Path
) -> list[Path]:
    """
    Recursively discover supported knowledge files.
    """

    directory = Path(directory)

    if not directory.exists():

        raise FileNotFoundError(
            f"Data directory does not exist: "
            f"{directory}"
        )

    files = []

    for path in directory.rglob("*"):

        if (
            path.is_file()
            and path.suffix.lower()
            in SUPPORTED_EXTENSIONS
        ):
            files.append(path)

    return sorted(files)


def load_json(
    path: Path
) -> list[dict]:

    with path.open(
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    if isinstance(data, dict):

        return [data]

    if isinstance(data, list):

        return data

    raise ValueError(
        f"JSON file must contain "
        f"an object or list: {path}"
    )


def load_text(
    path: Path
) -> list[dict]:

    content = path.read_text(
        encoding="utf-8"
    )

    return [
        {
            "title": path.stem,
            "content": content,
            "source": str(path)
        }
    ]


def load_file(
    path: Path
) -> list[dict]:

    suffix = path.suffix.lower()

    if suffix == ".json":

        return load_json(path)

    if suffix in {
        ".md",
        ".markdown",
        ".txt"
    }:

        return load_text(path)

    raise ValueError(
        f"Unsupported file type: {path}"
    )


def load_directory(
    directory: str | Path
) -> list[dict]:

    files = discover_files(
        directory
    )

    documents = []

    for path in files:

        loaded = load_file(path)

        for document in loaded:

            document["_source_file"] = str(
                path
            )

            documents.append(
                document
            )

    return documents
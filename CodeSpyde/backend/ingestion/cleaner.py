import re


def normalize_whitespace(
    text: str
) -> str:

    text = text.replace(
        "\r\n",
        "\n"
    )

    text = text.replace(
        "\r",
        "\n"
    )

    # Remove trailing whitespace.

    text = re.sub(
        r"[ \t]+$",
        "",
        text,
        flags=re.MULTILINE
    )

    # Collapse excessive blank lines.

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text
    )

    return text.strip()


def clean_text(
    text: str
) -> str:

    if not text:
        return ""

    text = str(text)

    # Remove common HTML tags.

    text = re.sub(
        r"<[^>]+>",
        " ",
        text
    )

    # Normalize spaces.

    text = normalize_whitespace(
        text
    )

    return text


def clean_document(
    document: dict
) -> dict:

    cleaned = {}

    for key, value in document.items():

        if isinstance(value, str):

            cleaned[key] = clean_text(
                value
            )

        else:

            cleaned[key] = value

    return cleaned
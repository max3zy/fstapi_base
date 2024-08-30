import re


TABS_REGEXP_TEXT = r'[\n\t\r]+'
TABS_REGEXP = re.compile(TABS_REGEXP_TEXT)
TAGS_REGEXP_TEXT = r'(\<(/?[^>]+)>)'
TAGS_REGEXP = re.compile(TAGS_REGEXP_TEXT)
SYMBOLS_REGEXP_TEXT = r"[^a-zа-я0-9]"
SYMBOLS_REGEXP = re.compile(SYMBOLS_REGEXP_TEXT)
SYMBOLS_WITHDASH_REGEXP_TEXT = r"(\s\-\s)|(\-\s)|(\s\-)|([^a-zа-я0-9\-])"
SYMBOLS_WITHDASH_REGEXP = re.compile(
    SYMBOLS_WITHDASH_REGEXP_TEXT
)
SPACES_REGEXP_TEXT = r"\s+"
SPACES_REGEXP = re.compile(SPACES_REGEXP_TEXT)
HTML_REGEXP_TEXT = r"(\<(/?[^>]+)>)"
HTML_REGEXP = re.compile(HTML_REGEXP_TEXT)


def text_cleanup_preprocessor(text: str, keep_dash: bool = False) -> str:
    result = str(text)
    result = result.lower()
    result = result.replace("ё", "е")
    result = TABS_REGEXP.sub(" ", result)
    result = TAGS_REGEXP.sub(" ", result)
    if keep_dash:
        result = SYMBOLS_WITHDASH_REGEXP.sub(" ", result)
    else:
        result = SYMBOLS_REGEXP.sub(" ", result)
    result = result.strip()
    result = SPACES_REGEXP.sub(" ", result)
    return result


def clean_html(text: str) -> str:
    """
    Удаление html-тегов (производится перед text_cleanup_preprocessor,
    если текст может содержать теги)
    """
    text = HTML_REGEXP.sub(' ', text)
    return SPACES_REGEXP.sub(' ', text).strip()
from re import sub


def compile_patterns():
    patterns = [
        (r'(["\'])(.*?)(\1)', r'«\2»'), # ёлочки
        (r'( - )', ' — '), # Дефисы с пробелами на тире
        (r'(\d{1,4})-', r'\1–'), # номера телефонов и промежуток лет
        (r'(\d)-([^\W|\d])', r'\1–\2'), #связывание чисел с последующими словами неразрывным дефисом
        (r'[ ]{2,}', r' '), # удаление лишних пробелов
        (r'\r\n', r'\n'),  # удаление лишних пустых строк Windows
        (r'\n{2,}', r'\n'),  # удаление лишних пустых строк Unix
        (r'(\b[^\W|\d]{1,2}) (\w)', r'\1 \2'),  # связывание слов из 1-2 символов

    ]
    return patterns


def typo_text(text):
    patterns = compile_patterns()
    for what_is_substituded, for_what in patterns:
        text = sub(what_is_substituded, for_what, text)
    return text


if __name__ == "__main__":
    pass
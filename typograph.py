from re import compile


def compile_patterns():
    patterns = [
        (compile(r'(["\'])(.*?)(\1)'), r'«\2»'), # ёлочки
        (compile(r'( - )'), ' — '), # Дефисы с пробелами на тире
        (compile(r'(\d{1,4})-'), r'\1–'), # номера телефонов и промежуток лет
        (compile(r'(\d)-([^\W|\d])'), r'\1–\2'), #связывание чисел с последующими словами неразрывным дефисом
        (compile(r'[ ]+'), r' '), # удаление лишних пробелов
        (compile(r'\n+'), r'\n'), # удаление лишних пустых строк
        (compile(r'(\b[^\W|\d]{1,2}) (\w)'), r'\1 \2'),  # связывание слов из 1-2 символов

    ]
    return patterns


def typo_text(text):
    patterns = compile_patterns()
    for pattern in patterns:
        text = pattern[0].sub(pattern[1], text)
    return text


if __name__ == "__main__":
    pass
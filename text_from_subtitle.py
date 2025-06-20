import re
from deep_translator import GoogleTranslator

def extract_subtitle_text_with_translation(srt_path, output_path):
    translator = GoogleTranslator(source='en', target='ru')

    with open(srt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    subtitle_text = []
    buffer = []

    for line in lines:
        line = line.strip()
        if not line or line.isdigit() or '-->' in line:
            if buffer:
                original = ' '.join(buffer)
                try:
                    translated = translator.translate(original)
                except Exception as e:
                    translated = '[Ошибка перевода]'
                subtitle_text.append(original)
                subtitle_text.append('— ' + translated)
                subtitle_text.append('')  # пустая строка между репликами
                buffer = []
            continue
        buffer.append(line)

    # не забываем про остаток
    if buffer:
        original = ' '.join(buffer)
        try:
            translated = translator.translate(original)
        except Exception as e:
            translated = '[Ошибка перевода]'
        subtitle_text.append(original)
        subtitle_text.append('— ' + translated)

    # Запись в файл
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(subtitle_text))

def extract_unique_words(input_path, output_path_words, output_path_translated):
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = sorted(set(words))

    # Сохраняем список слов
    with open(output_path_words, 'w', encoding='utf-8') as f:
        f.write('\n'.join(unique_words))

    # Переводим слова
    translator = GoogleTranslator(source='en', target='ru')
    translations = {}
    for word in unique_words:
        try:
            ru = translator.translate(word)
            translations[word] = ru
        except Exception as e:
            print(f"Ошибка при переводе '{word}': {e}")
            translations[word] = 'Ошибка'

    # Сохраняем переводы
    with open(output_path_translated, 'w', encoding='utf-8') as f:
        for en, ru in translations.items():
            f.write(f"{en} — {ru}\n")

extract_subtitle_text_with_translation("./subtitles/subtitle_7_und.srt", "./dialogue.txt")
#extract_unique_words("./dialogue.txt", "./unique_words.txt", "./translated_words.txt")


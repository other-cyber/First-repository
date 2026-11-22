import re
from collections import Counter


# Разделает текст на отдельные слова
def definition(text):
    split_text = re.split(r"[,:;!. ]", text)
    return split_text


# Подсчитывает количество слов
def word_count(clean_split_text):
    c_list = Counter(clean_split_text)
    return c_list, len(clean_split_text)


# Ищет уникальные слова
def unique_words(c_list):
    unique_list = [k for k, v in c_list.items() if v == 1]
    return unique_list


# Ищет самое частое слово
def freq_enc(c_list):
    count_freq = max(c_list.values())
    word = next(k for k, v in c_list.items() if v == count_freq)
    return count_freq, word


# Подсчитывает среднюю длину слова
def aver_word_length(clean_split_text):
    length_word = 0
    for i in clean_split_text:
        length_word += len(i)
    length_word /= len(clean_split_text)
    return length_word


def find_words_repeated_twice(c_list):
    list_word = [k for k, v in c_list.items() if v == 2]
    return list_word


def main():
    text = input("Введите текст: ")
    split_text = definition(text)
    split_text = [x.lower() for x in split_text]
    clean_split_text = [x for x in split_text if x != ""]
    c_list, count_word = word_count(clean_split_text)
    unique_list = unique_words(c_list)
    count_freq, freq_word = freq_enc(c_list)
    avg_word = aver_word_length(clean_split_text)
    list_word = find_words_repeated_twice(c_list)
    print(f"Количество слов - {count_word}")
    print(f"Уникальных слов {len(unique_list)}")
    print(f"Самое часто встречающаеся слово - {freq_word}, количество {count_freq} ")
    print(f"Средняя длина слова: {avg_word}")
    print(f"Список слов, которые встречаются ровно 2 раза: {list_word}")


main()

import re
import csv

if __name__ == "__main__":
    file = open("Frankenstein.txt", "r", encoding="utf-8-sig")
    word_dict = {}
    for line in file:
        for word in line.split():
            cword = re.sub("[^a-zA-Z]+", "", word)  # Remove non-alphanumeric characters
            cword = cword.capitalize()

            if not cword:
                continue
            if cword not in word_dict:
                word_dict[cword] = 1
            else:
                word_dict[cword] += 1
    file.close()

    csv_file = open("word_count.csv", "w", encoding="utf-8-sig")
    write = csv.writer(csv_file)
    write.writerow(["word", "count"])
    write.writerows(word_dict.items())
    csv_file.close()

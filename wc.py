import sys
import os

file = open("art_of_war.txt", encoding= "utf-8")
lines = file.readlines()
file.close()

file_name = "art_of_war.txt"
file_stats = os.stat(file_name)

def number_of_lines():
    return len(lines)

def number_of_words():
    count_words = 0
    for line in lines:
        words = line.split()
        count_words += len(words)
    return count_words

def number_of_characters():
    return (sum(len(i) for i in lines))

def number_of_bytes():
    return (f'File Size in Bytes is {file_stats.st_size}')

if sys.argv[1] == "-l":
    print(str(number_of_lines()))

if sys.argv[1] == "-w":
    print(str(number_of_words()))

if sys.argv[1] == "-m":
    print(str(number_of_characters()))

if sys.argv[1] == "-c":
    print(str(number_of_bytes()))
    
if sys.argv[1] == "art_of_war.txt":
    print(str(number_of_lines()), str(number_of_words()), str(number_of_characters()))
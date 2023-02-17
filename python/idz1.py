#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Написать программу, которая считывает текст из файла и выводит на экран сначала
вопросительные, а затем восклицательные предложения.
"""

if __name__ == "__main__":
    exclamation_sentences = []
    question_sentences = []

    with open("test_for_Idz1.txt", "r", encoding="utf-8") as f:
        sentences = f.readlines()

        for i in sentences:
            if i.find("!") != -1:
                exclamation_sentences.append(i)
            if i.find("?") != -1:
                question_sentences.append(i)

        print(*question_sentences)
        print("---------------")
        print(*exclamation_sentences)

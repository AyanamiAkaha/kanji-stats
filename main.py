#!/usr/bin/env python3

import os
import argparse

def get_novels(path):
    novels = os.listdir(path)
    return [os.path.join(path, novel) for novel in novels]

def get_novel(path):
    novel = ""
    files = os.listdir(path)
    for file in files:
        with open(os.path.join(path, file), "r") as f:
            novel += f.read()
    return novel

def kanji_stats(novel, kanji_list):
    kanji = {}
    for char in novel:
        if char in kanji_list:
            if char in kanji:
                kanji[char] += 1
            else:
                kanji[char] = 1
    return kanji

def summary(path, kanji_stats, kanji_list):
    summary = {
        "path": path,
        "missing": "",
        "counts": {},
        "total_seen": 0,
        "total_missing": 0
    }
    for char in kanji_list:
        if char in kanji_stats:
            summary["counts"][char] = kanji_stats[char]
            summary["total_seen"] += 1
        else:
            summary["missing"] += char
            summary["total_missing"] += 1
    return summary

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", metavar="path", help="Path to the novels", required=True)
    parser.add_argument("-k", "--kanji", metavar="kanji", help="Path to the kanji list", required=True)
    args = parser.parse_args()
    path = args.path
    kanji_fname = args.kanji
    kanji_list = ""
    with open(kanji_fname, "r") as f:
        kanji_list = f.read()
        if "\n" in kanji_list:
            kanji_list = kanji_list.replace("\n", "")
    novels = get_novels(path)
    summaries = [summary(path, kanji_stats(get_novel(path), kanji_list), kanji_list) for path in novels]
    sorted_summaries = sorted(summaries, key=lambda x: x["total_seen"], reverse=True)
    for stat in sorted_summaries:
        print("------")
        print(stat["path"] + "\n")
        print("Kanji:")
        for v in sorted(stat["counts"].items(), key=lambda x: x[1], reverse=True):
            print(v[0] + ": " + str(v[1]))
        print("\nMissing:")
        print(stat["missing"])
        print("\nTotal seen: " + str(stat["total_seen"]))
        print("Total missing: " + str(stat["total_missing"]))
        print()

if __name__ == "__main__":
    main()
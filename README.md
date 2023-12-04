A simple script that calculates kanji statistics in novels.

Required folder structure:

```
novels_root/
    novel1/
        chapter1.txt
        chapter2.txt
    novel2/
        chapter1.txt
...
```

file names are not important.

On top of that you need to prepare a text file with all the kanji you're
interested in. Then run:

```
./main.py -p /path/to/novels_root -k /path/to/kanji_list_file
```
The script will calculate the stats in each novel, and print to stdout,
sorting by kanji list coverage. In other words, first in the output will
be the novel that uses the most kanji from provided list file.

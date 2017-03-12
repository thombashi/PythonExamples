# Summary
A sample program to read a CSV file.
This program works for both Python 2/3.


# Read a CSV file (ascii)
```bash
$ ./csv_read.py sample_ascii.csv
--- header ---
['Country or Area', 'Year', 'Area', 'Sex', 'Record Type', 'Reliability', 'Source Year', 'Value', 'Value Footnotes']

--- data ---
['Afghanistan', '2014', 'Total', 'Both Sexes', 'Estimate - de facto', 'Final figure, incomplete/questionable reliability', '2015', '26556754', '1']
['Afghanistan', '2014', 'Total', 'Male', 'Estimate - de facto', 'Final figure, incomplete/questionable reliability', '2015', '13585933', '1']
['Afghanistan', '2014', 'Total', 'Female', 'Estimate - de facto', 'Final figure, incomplete/questionable reliability', '2015', '12970821', '1']
```

# Read a CSV file (utf-8)
```bash
$ ./csv_read.py sample_utf8.csv
--- header ---
['dataset_id', 'year', 'publisher', 'group_title', 'frequency_of_update', 'data_format', 'language', 'resource_count']

--- data ---
['12971', '2015', '消費者庁', '行財政', '年単位', 'PDF', '英語', '1']
['12971', '2015', '消費者庁', '行財政', '年単位', 'HTML', '日本語', '59']
['12971', '2015', '消費者庁', '行財政', '年単位', 'PDF', '日本語', '4']
['12972', '2015', '消費者庁', '行財政', '年単位', 'HTML', '日本語', '3']
['12972', '2015', '消費者庁', '行財政', '年単位', 'PDF', '日本語', '6']
['12973', '2015', '消費者庁', '行財政', '年単位', 'PDF', '日本語', '6']
['12974', '2015', '消費者庁', '行財政', '年単位', 'PDF', '日本語', '4']
['12975', '2015', '消費者庁', '行財政', 'その他（自由記述）', 'PDF', '日本語', '7']
['12976', '2015', '消費者庁', '行財政', 'その他（自由記述）', 'PDF', '日本語', '4']
```

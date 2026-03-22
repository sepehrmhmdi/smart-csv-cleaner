# Smart CSV Cleaner

A simple Python CLI tool to automatically clean messy CSV files.

## Features

* Remove empty rows
* Remove duplicates
* Trim unnecessary spaces
* Normalize date formats
* Drop rows with missing values in specific columns
* Optional lowercase normalization
* Detailed cleaning report

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python cleaner.py sample_dirty.csv cleaned.csv \
  --dedup email \
  --drop-missing email \
  --lowercase \
  --normalize-dates
```

---

## Example Output

```
📊 CLEANING REPORT
------------------------------
✔ Initial rows        : 9
✔ Final rows          : 5
✔ Removed rows        : 4
  ↳ empty rows        : 1
  ↳ duplicates        : 2
  ↳ missing values    : 1
```

---

## Sample Data

The file `sample_dirty.csv` intentionally contains:

* duplicate rows
* inconsistent date formats
* extra spaces
* missing values

---

## Purpose

This project demonstrates how to build a simple but practical tool for cleaning real-world CSV data using Python.



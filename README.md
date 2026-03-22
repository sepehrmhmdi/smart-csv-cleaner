# Smart CSV Cleaner

A simple Python CLI tool to clean and preprocess messy CSV files.

## Features

* Remove empty rows
* Remove duplicates
* Trim unnecessary spaces
* Normalize date formats
* Drop rows with missing values in specific columns
* Optional lowercase normalization
* Detailed cleaning report

---

## Demo

![csv-cleaner demo](/assets/demo_nord.gif)

<sub>Demo recorded using <a href="https://github.com/sepehrmhmdi/termogen">Termogen</a></sub>

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python3 cleaner.py sample_dirty.csv cleaned.csv \
  --dedup email \
  --drop-missing email \
  --lowercase \
  --normalize-dates
```

---

## Example Output

```
CLEANING REPORT
------------------------------
Initial rows        : 9
Final rows          : 5
Removed rows        : 4
  empty rows        : 1
  duplicates        : 2
  missing values    : 1
```

---

## Sample Data

The file `sample_dirty.csv` intentionally includes:

* duplicate rows
* inconsistent date formats
* extra spaces
* missing values

---

## Purpose

This project demonstrates how to build a simple and practical tool for cleaning real-world CSV data using Python.

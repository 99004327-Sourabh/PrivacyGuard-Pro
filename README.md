# CIS 6930 Spring 2024 Assignment 1: The Censoror

## Introduction

The Censoror is a Python application developed for CIS 6930 Spring 2024, designed to automate the redaction of sensitive information from plain text documents. This tool ensures privacy and compliance with data protection standards, making it ideal for processing documents with sensitive content such as police reports, court transcripts, and hospital records. For testing and demonstration, the project uses the Enron Email Dataset.

## Prerequisites

Before you begin, ensure you have installed:

- Python 3.11
- Pipenv

## Installation

Follow these steps to set up The Censoror on your local machine:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/99004327-Sourabh/cis6930sp24-assignment1.git
    cd cis6930sp24-assignment1
    ```

2. **Install Dependencies:**
    ```bash
    pipenv install
    ```

## Parameters

- `--input`: Specifies the glob pattern for input files. This allows the program to process multiple files at once based on the pattern provided.
- `--output`: Designates the directory where censored files will be stored. Each censored file will be saved in this directory with the original filename plus a `.censored` extension.
- `--names`, `--dates`, `--phones`, `--address`: Flags to indicate which types of sensitive information should be censored. Each flag enables the detection and redaction of a specific type of sensitive information:
  - `--names`: Censors personal names found in the text.
  - `--dates`: Censors date expressions.
  - `--phones`: Censors phone numbers.
  - `--address`: Censors physical addresses.
- `--stats`: Defines where to output statistics of the censorship process. This can be the name of a file where statistics will be written, or special keywords `stderr` or `stdout` to output the statistics to the standard error or standard output streams, respectively.

## Dataset

For testing, utilize the Enron Email Dataset with the following commands:

```bash
wget https://www.cs.cmu.edu/~enron/enron_mail_20150507.tar.gz
tar xvzf enron_mail_20150507.tar.gz -C /tmp
```

## Submission Files

Your submission should include the following files:

- `README.md`: This file, providing an overview and instructions for using the project.

## Testing

To ensure The Censoror functions as expected, execute tests using the following command:

```bash
pipenv run python -m pytest
```
## License

This project is licensed under the MIT License. For more details, see the `LICENSE.md` file.






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

## Usage

Run The Censoror using the following command:

```bash
pipenv run python censoror.py --input '*.txt' \
                              --names --dates --phones --address \
                              --output 'files/' \
                              --stats stderr
## Parameters

- `--input`: Specifies the glob pattern for input files. This allows the program to process multiple files at once based on the pattern provided.
- `--output`: Designates the directory where censored files will be stored. Each censored file will be saved in this directory with the original filename plus a `.censored` extension.
- `--names`, `--dates`, `--phones`, `--address`: Flags to indicate which types of sensitive information should be censored. Each flag enables the detection and redaction of a specific type of sensitive information:
  - `--names`: Censors personal names found in the text.
  - `--dates`: Censors date expressions.
  - `--phones`: Censors phone numbers.
  - `--address`: Censors physical addresses.
- `--stats`: Defines where to output statistics of the censorship process. This can be the name of a file where statistics will be written, or special keywords `stderr` or `stdout` to output the statistics to the standard error or standard output streams, respectively.


bash
Copy code
wget https://www.cs.cmu.edu/~enron/enron_mail_20150507.tar.gz
tar xvzf enron_mail_20150507.tar.gz -C /tmp
Submission Files
Your submission should include the following files:

README.md: This file, containing an overview and instructions for using the project.
COLLABORATORS: A file detailing any collaboration that occurred during the assignment.
Testing
To ensure The Censoror functions as expected, run tests with:

bash
Copy code
pipenv run python -m pytest
Ensure your tests comprehensively cover all functionalities of the application.

Contributing
Contributions to The Censoror are welcome. Follow these steps to contribute:

Fork the repository.
Create a new feature branch (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -am 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE.md file for more details.

Acknowledgments
Enron Email Dataset for providing a real-world dataset for testing.
The instructors and TAs of CIS 6930 for their guidance and support.
Contact
Your Name: [Insert Your Name]
Email: [Insert Your Email]
Project Link: https://github.com/99004327-Sourabh/cis6930sp24-assignment1

import re
import os
import spacy
import glob
import sys
from collections import defaultdict
import en_core_web_trf

# Load the spaCy model
from assignment1.parse_args import parse_args

nlp = en_core_web_trf.load()


def censor_names_and_dates(text, censor_names, censor_dates):
    stats = defaultdict(
        int, {"names": 0, "dates": 0, "phones": 0, "addresses": 0, "positions": []}
    )
    doc = nlp(text)
    for ent in reversed(doc.ents):
        if (censor_names and ent.label_ == "PERSON") or (
            censor_dates and ent.label_ == "DATE"
        ):
            text = text[: ent.start_char] + "█" * len(ent.text) + text[ent.end_char :]
            stats["positions"].append((ent.start_char, ent.end_char))
            if ent.label_ == "PERSON":
                stats["names"] += 1
            else:
                stats["dates"] += 1
    return text, stats


def censor_phone_numbers(text):
    phone_pattern = r"""
    (?:(?<![\d-])(?:\+?\d{1,3}[-.\s*]?)?(?:\(?\d{3}\)?[-.\s*]?)?\d{3}[-.\s*]?\d{4}(?![\d-]))|
    (?:(?<![\d-])(?:(?:\(\+?\d{2}\))|(?:\+?\d{2}))\s*\d{2}\s*\d{3}\s*\d{4}(?![\d-]))
    """
    censored_text = re.sub(phone_pattern, "█" * 12, text, flags=re.VERBOSE)
    return censored_text, {
        "phones": len(re.findall(phone_pattern, text, flags=re.VERBOSE))
    }


def censor_dates(text):
    date_pattern = re.compile(
        r"""
        (?:Mon|Tue|Wed|Thu|Fri|Sat|Sun),\s\d{1,2}\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}(?:\s\d{2}:\d{2}(?::\d{2})?\s(?:-\d{4}|\+\d{4}|[A-Z]{2,3}))?
        |\b\d{1,2}\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}\b
        |\b\d{1,2}[-/\s](Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/\s]\d{2,4}\b
        |\b\d{1,2}[-/\s][0-1]?\d[-/\s]\d{2,4}\b
        |\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+\d{4}\b
        |\d{4}[-/\s](?:0[1-9]|1[0-2])[-/\s](?:0[1-9]|[12][0-9]|3[01])
        """,
        re.VERBOSE | re.IGNORECASE,
    )

    censored_text = re.sub(date_pattern, "█" * 10, text)
    return censored_text, {
        "dates": len(re.findall(date_pattern, text, flags=re.VERBOSE | re.IGNORECASE))
    }


def censor_addresses(text):
    address_pattern = r"\b\d{1,5}\s(?:\w+\s){1,2}(Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Drive|Dr|Lane|Ln|Court|Ct)\b|\bP\.O\. Box \d{1,5}\b|\b(?:[A-Za-z]+\s?){1,3},\s[A-Z]{2}\s\d{5}(-\d{4})?\b"
    censored_text = re.sub(address_pattern, "█" * 10, text)
    return censored_text, {"addresses": len(re.findall(address_pattern, text))}


def output_stats(stats, statsMode):
    stats_str = "Files processed: {}\nNames redacted: {}\nDates redacted: {}\nPhone numbers redacted: {}\nAddresses redacted: {}\nPositions redacted: {}".format(
        stats["files_processed"],
        stats["names"],
        stats["dates"],
        stats["phones"],
        stats["addresses"],
        stats["positions"],
    )
    if statsMode == "stdout" or statsMode is None:
        sys.stdout.write(stats_str)
    elif statsMode == "stderr":
        sys.stderr.write(stats_str)
    else:
        with open(statsMode, "w") as f:
            f.write(stats_str)


def process_files(args):
    overall_stats = defaultdict(
        int,
        {
            "files_processed": 0,
            "names": 0,
            "dates": 0,
            "phones": 0,
            "addresses": 0,
            "positions": [],
        },
    )
    # absoluteFilePaths1 = [os.path.abspath(path) for path in args.input]
    # absoluteFilePaths2 = os.path.abspath(args.output)
    # print(absoluteFilePaths1)
    # print(absoluteFilePaths2)
    filePathList = []
    inputPattern = args.input
    file_paths = glob.glob(inputPattern)
    absoluteFilePaths1 = [os.path.abspath(path) for path in file_paths]
    absoluteFilePaths2 = os.path.abspath(args.output)
    print(absoluteFilePaths1)
    print(absoluteFilePaths2)
    for input in absoluteFilePaths1:
        file_path = glob.glob(input)
        filePathList.extend(file_path)

    for file_path in filePathList:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        censored_text, name_and_date_stats = censor_names_and_dates(
            text, args.names, args.dates
        )
        overall_stats["names"] += name_and_date_stats["names"]
        overall_stats["dates"] += name_and_date_stats["dates"]
        overall_stats["positions"].extend(name_and_date_stats["positions"])

        censored_text, phone_stats = censor_phone_numbers(censored_text)
        overall_stats["phones"] += phone_stats["phones"]

        censored_text, address_stats = censor_addresses(censored_text)
        overall_stats["addresses"] += address_stats["addresses"]

        overall_stats["files_processed"] += 1

        output_file_path = os.path.join(
            absoluteFilePaths2, os.path.basename(file_path) + ".censored"
        )
        os.makedirs(absoluteFilePaths2, exist_ok=True)
        with open(output_file_path, "w", encoding="utf-8") as censored_file:
            censored_file.write(censored_text)
    statsMode = args.stats
    output_stats(overall_stats, statsMode)


# Main function and argument parsing would go here
def main():
    args = parse_args()
    process_files(args)


if __name__ == "__main__":
    main()

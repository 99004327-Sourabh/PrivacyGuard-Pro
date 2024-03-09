import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Censor sensitive information from text documents."
    )
    parser.add_argument(
        "--input", required=True, type=str, help="Glob pattern for input text files."
    )

    parser.add_argument("--names", action="store_true", help="Flag to censor names.")
    parser.add_argument("--dates", action="store_true", help="Flag to censor dates.")
    parser.add_argument(
        "--phones", action="store_true", help="Flag to censor phone numbers."
    )
    parser.add_argument(
        "--address", action="store_true", help="Flag to censor addresses."
    )
    parser.add_argument(
        "--output",
        required=True,
        type=str,
        help="Directory to store censored output files.",
    )
    parser.add_argument(
        "--stats", type=str, help="File or STDOUT/STDERR to output statistics."
    )
    return parser.parse_args()

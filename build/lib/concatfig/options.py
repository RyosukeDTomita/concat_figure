# coding: utf-8
import argparse


def parse_args() -> dict:
    """parse_args.

    Args:

    Returns:
        dict:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="set csvfile.",
                        type=str)
    p = parser.parse_args()
    args = {"file": p.file}
    return args

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
    parser.add_argument("-s", "--save", help="save file name.",
                        type=str)
    parser.add_argument("-p", "--path", help="csvfile express figure path.",
            action="store_true")
    p = parser.parse_args()
    args = {"file": p.file, "save": p.save, "path": p.path}
    return args

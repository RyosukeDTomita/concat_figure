"""
Name: concat_fig.py

Concat multiply figure.

Usage: python3 concat.py --file <csv file>

Author: Ryosuke Tomita
Date: 2022/01/17
"""
import argparse
import csv
from os.path import abspath, dirname, join
import dataclasses
import pandas as pd
from PIL import Image

def parse_args() -> dict:
    """parse_args.
    set file path.

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


def to_abs_path(csv_file_path: str, fig_path: str) -> str:
    return join(abspath(dirname(csv_file_path)), fig_path)


@dataclasses.dataclass
class ConcatFig:
    """ConcatFig.
    """

    def cat_vertical(self, img_upper, img_lower):
        cated_img = Image.new('RGB',
                (max(img_upper.width, img_lower.width),
                    img_upper.height + img_lower.height
                ),
        )
        cated_img.paste(img_upper, (0, 0))
        cated_img.paste(img_lower, (0, img_upper.height))
        return cated_img

    def cat_horizontal(self, img_right, img_left):
        cated_img = Image.new('RGB',
                (img_right.width + img_left.width,
                    max(img_right.height,img_left.height)
                ),
        )
        cated_img.paste(img_left, (0, 0))
        cated_img.paste(img_right, (img_left.width, 0))
        return cated_img


def main():
    args = parse_args()

    concat_fig = ConcatFig()
    df = pd.read_csv(args["file"], header=None)
    horizontal_len = len(df.values[0])
    vertical_len = len(df.values)
    cated_h_figs = []

    for v in range(vertical_len):
        for h in range(0, horizontal_len):
            print(df[h][v])
            if   h == horizontal_len - 1:
                break
            elif h == 0:
                img_right = Image.open(to_abs_path(args["file"], df[h+1][v]))
                img_left = Image.open(to_abs_path(args["file"], df[h][v]))
                img_left = concat_fig.cat_horizontal(img_right, img_left)
            else:
                img_right = Image.open(to_abs_path(args["file"], df[h+1][v]))
                img_left = concat_fig.cat_horizontal(img_right, img_left)
        cated_h_figs.append(img_left)

    for v in range(len(cated_h_figs)):

        if   v == len(cated_h_figs) -1:
            break
        elif v == 0:
            img_upper = cated_h_figs[v]
            img_lower = cated_h_figs[v+1]
            img_upper = concat_fig.cat_vertical(img_upper, img_lower)
        else:
            img_lower = cated_h_figs[v+1]
            img_upper = concat_fig.cat_vertical(img_upper, img_lower)
    img_upper.save("tmp.png")


if __name__ == "__main__":
    main()

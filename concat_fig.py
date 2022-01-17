"""
Name: concat_fig.py

Concat multiply figure.

Usage: python3 concat.py --file <csv file>

Author: Ryosuke Tomita
Date: 2022/01/17
"""
import argparse
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
    """to_abs_path.

    Args:
        csv_file_path (str): csv_file_path
        fig_path (str): fig_path

    Returns:
        str:
    """
    return join(abspath(dirname(csv_file_path)), fig_path)


@dataclasses.dataclass
class ConcatFig:
    """ConcatFig.
    """
    csvfile: str

    def __post_init__(self):
        """__post_init__.
        """
        self.df = pd.read_csv(self.csvfile, header=None)
        self.df_h_len = len(self.df.values[0])
        self.df_v_len = len(self.df.values)

    def cat_vertical(self, img_upper, img_lower):
        """cat_vertical.

        Args:
            img_upper:
            img_lower:
        """
        cated_img = Image.new('RGB',
                (max(img_upper.width, img_lower.width),
                    img_upper.height + img_lower.height
                ),
        )
        cated_img.paste(img_upper, (0, 0))
        cated_img.paste(img_lower, (0, img_upper.height))
        return cated_img

    def cat_horizontal(self, img_right, img_left):
        """cat_horizontal.

        Args:
            img_right:
            img_left:
        """
        cated_img = Image.new('RGB',
                (img_right.width + img_left.width,
                    max(img_right.height,img_left.height)
                ),
        )
        cated_img.paste(img_left, (0, 0))
        cated_img.paste(img_right, (img_left.width, 0))
        return cated_img

    def cat_all(self) -> Image.Image:
        """cat_all.

        Args:

        Returns:
            Image.Image:
        """
        cated_h_figs = []

        # concated figures horizontaly.
        for v in range(self.df_v_len):
            for h in range(self.df_h_len):
                print(self.df[h][v])
                if h == self.df_h_len - 1:
                    continue
                if h == 0:
                    img_right = Image.open(to_abs_path(self.csvfile, self.df[h+1][v]))
                    img_left = Image.open(to_abs_path(self.csvfile, self.df[h][v]))
                    img_left =self.cat_horizontal(img_right, img_left)
                else:
                    img_right = Image.open(to_abs_path(self.csvfile, self.df[h+1][v]))
                    img_left =self.cat_horizontal(img_right, img_left)
            cated_h_figs.append(img_left)
        # concat figures created by cat_horizontal() vertically.
        for v in range(len(cated_h_figs)):

            if v == len(cated_h_figs) -1:
                continue
            if v == 0:
                img_upper = cated_h_figs[v]
                img_lower = cated_h_figs[v+1]
                img_upper =self.cat_vertical(img_upper, img_lower)
            else:
                img_lower = cated_h_figs[v+1]
                img_upper =self.cat_vertical(img_upper, img_lower)
        cated_fig = img_upper
        return cated_fig


def main():
    """main.
    """
    args = parse_args()

    concat_fig = ConcatFig(args["file"])
    cated_fig = concat_fig.cat_all()
    cated_fig.save("tmp.png")


if __name__ == "__main__":
    main()

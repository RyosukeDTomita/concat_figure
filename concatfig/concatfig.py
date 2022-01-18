# coding: utf-8
from os.path import abspath, dirname, join
import dataclasses
import pandas as pd
from PIL import Image
from concatfig.hvcat import cat_horizontal, cat_vertical


@dataclasses.dataclass
class ConcatFig:
    """ConcatFig.
    """
    csvfile: str
    use_rpath: bool = False

    def __post_init__(self):
        """__post_init__.
        """
        self.df = pd.read_csv(self.csvfile, header=None)
        self.df_h_len = len(self.df.values[0])
        self.df_v_len = len(self.df.values)

    def to_abs_path(self, fig_path: str):
        if self.use_rpath:
            return fig_path
        else:
            return join(abspath(dirname(self.csvfile)), fig_path)

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
                    img_right = Image.open(self.to_abs_path(self.df[h+1][v]))
                    img_left = Image.open(self.to_abs_path(self.df[h][v]))
                    img_left = cat_horizontal(img_right, img_left)
                else:
                    img_right = Image.open(self.to_abs_path(self.df[h+1][v]))
                    img_left = cat_horizontal(img_right, img_left)
            cated_h_figs.append(img_left)
        # concat figures created by cat_horizontal() vertically.
        for v in range(len(cated_h_figs)):

            if v == len(cated_h_figs) -1:
                continue
            if v == 0:
                img_upper = cated_h_figs[v]
                img_lower = cated_h_figs[v+1]
                img_upper = cat_vertical(img_upper, img_lower)
            else:
                img_lower = cated_h_figs[v+1]
                img_upper = cat_vertical(img_upper, img_lower)
        cated_fig = img_upper
        return cated_fig

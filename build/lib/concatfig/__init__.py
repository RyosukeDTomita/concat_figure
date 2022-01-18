# coding: utf-8
from concatfig import concatfig
from .options import parse_args


def main():
    args = parse_args()

    concat_fig = concatfig.ConcatFig(args["file"])
    cated_fig = concat_fig.cat_all()
    cated_fig.save("tmp.png")

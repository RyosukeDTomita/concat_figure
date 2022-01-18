# coding: utf-8
from concatfig import concatfig
from .options import parse_args


def main():
    args = parse_args()

    concat_fig = concatfig.ConcatFig(args["file"],
            use_rpath=args["rpath"])
    cated_fig = concat_fig.cat_all()

    if args["save"] == None:
        cated_fig.save("concat.png")
    else:
        cated_fig.save(args["save"])

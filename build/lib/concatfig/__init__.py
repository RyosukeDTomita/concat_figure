# coding: utf-8
from concatfig import ConcatFig
from .options import parse_args


def main():
    args = parse_args()

    concat_fig = ConcatFig.ConcatFig(args["file"],
            use_path=args["path"])
    cated_fig = concat_fig.cat_all()

    if args["save"] == None:
        cated_fig.save("concat.png")
    else:
        cated_fig.save(args["save"])

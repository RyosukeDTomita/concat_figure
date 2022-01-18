# INDEX
- [ABOUT](#ABOUT)
- [HOWTOUSE](#HOWTOUSE)
- [INSTALATION](#INSTALATION)
- [ENVIRONMENT](#ENVIRONMENT)

# ABOUT
This program can concat figures by order which csvfile order.

```
2021-01-06_12_ldr24.png,2021-01-07_00_ldr24.png,2021-01-07_12_ldr24.png
2021-01-06_12_850.png,2021-01-07_00_850.png,2021-01-07_12_850.png
2021-01-06_12_500.png,2021-01-07_00_500.png,2021-01-07_12_500.png
2021-01-06_12_300.png,2021-01-07_00_300.png,2021-01-07_12_300.png
```
![concat.png](./tryme/concat.png)

# HOWTOUSE
- figures are saved the directory which saved `csvfile`.
- `csvfile` express the order of figures.
- if `--save`is not set, default output name is `concat.png`.
- -p: csvfile contents expressed figure path.

```shell
python3 concat_fig.py --file ./tryme/sample.csv --save <save file name>
python3 concat_fig.py --file ./tryme/sample.csv --save <save file name> -p
```

# INSTALATION
## Install

```
python3 setup.py install
```

## uninstall

```shell
python setup.py develop -u
pip uninstall concatfig
```

# ENVIRONMENT
I tested the following environment.
- Python3.8
- Ubuntu 20.04 LTS
see [requirement.txt](./requirements.txt)

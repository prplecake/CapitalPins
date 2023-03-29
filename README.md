# CapitalPins

A small utility to rename Pinboard tags.

## Requirements

* Python >= 3
* Pinboard>=2.0
* PyYAML

Install dependencies with:

```shell
python -m pip install -r requirements.txt
```

## Usage

```text
usage: run.py [-h] [--dry-run] [-U] old_name [new_name]

Capitalize Pinboard tags.

positional arguments:
  old_name
  new_name

optional arguments:
  -h, --help   show this help message and exit
  --dry-run    Perform a dry run, doesn't change anything.
  -U, --upper  Renames the tag to an UPPERCASE string.
```

### Examples

```shell
python run.py tag_name
```

The new tag name would be `Tag_name`.

```shell
python run.py -U tag_name
```

The new tag name would be `TAG_NAME`.

```shell
python run.py old_tag new_tag
```

This would rename `old_tag` to `new_tag`. Useful for those pesky edge
cases.

# Checklist for common errors
## Simple solutions to try

- Verify sintax
- Copy / paste the error msg in Google and try Stack overflow most voted solution
- Update / upgrade version


## Some examples:

- Error:
A "pyproject.toml" file was found, but editable mode currently requires a setup.py based build
Ocurried when tried to make a new package in edition mode: `pip install -e .`

  - Solution:
  `python3 -m pip install --upgrade pip`
  And run `pip install -e .` again

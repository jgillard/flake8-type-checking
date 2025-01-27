import sys

ATTRIBUTE_PROPERTY = '_flake8-type-checking_parent'

ATTRS_DECORATORS = ['attrs.define', 'attr.define', 'attr.s']
ATTRS_IMPORTS = {'attrs', 'attr'}

py38 = sys.version_info.major == 3 and sys.version_info.minor == 8


# Error codes
TC001 = "TC001 Move application import '{module}' into a type-checking block"
TC002 = "TC002 Move third-party import '{module}' into a type-checking block"
TC003 = "TC003 Move built-in import '{module}' into a type-checking block"
TC004 = "TC004 Move import '{module}' out of type-checking block. Import is used for more than type hinting."
TC005 = 'TC005 Found empty type-checking block'
TC100 = "TC100 Add 'from __future__ import annotations' import"
TC101 = "TC101 Annotation '{annotation}' does not need to be a string literal"
TC200 = "TC200 Annotation '{annotation}' needs to be made into a string literal"
TC201 = "TC201 Annotation '{annotation}' does not need to be a string"

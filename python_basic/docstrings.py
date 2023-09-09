# docstrings

def get_name(first_name, last_name):
    """take first name and last name then return combine two"""
    if first_name == "":
        return "Your first name is missing ..."
    if last_name == "":
        return "Your last name is missing ..."
    return f"{first_name}, {last_name}"

print(get_name.__doc__)
print(help(get_name))

# WARNING ...
a = """
Hello World
"""
print(a)

# - Epytext
"""
This is a javadoc style.

@param fist_name: this is a first param
@param last_name: this is a second param
@returns: this is a desciption of what is returned
@raises keyError: raises an exception
"""

# - reST reStructuredText (reST) from Sphinx
"""
This is a reST style

:param fist_name: this is a first param
:param last_name: this is a second param
:returns: this is a desciption of what is returned
:raises keyError: raises an exception
"""

# - Google
"""
This is an exmple of Google style.

Args:
    param fist_name: this is a first param
    param last_name: this is a second param

Returns:
    this is a desciption of what is returned

Raises:
    keyError: raises an exception
"""

# - Numpydoc
"""
My numpydoc desciprtion of a kind

Parameters
-------------------
fist_name: this is a first param
last_name: this is a second param

Returns
--------------------
this is a desciption of what is returned

Raises
-------------------
keyError: raises an exception
"""

###############
pivot-to-python
###############

Components and examples from the Pivot to Python book.

Installation
=============

There are several steps to getting this ready for experimentation.

The book uses **uv**, https://astral.sh/blog/uv-unified-python-packaging.

Start by installing **uv**.
https://docs.astral.sh/uv/getting-started/installation/


1.  Clone or download this https://github.com/slott56/pivot-to-python.git repository.
    Use desktop ``git clone`` or the a GUI tool like GitHub Desktop https://desktop.github.com/download/.

    ..  code-block:: bash

        % git clone https://github.com/slott56/pivot-to-python.git

2.  Change to the downloaded directory.

    ..  code-block:: bash

        % cd pivot-to-python

3.  Initialize a UV project with Python 3.12

    ..  code-block:: bash

        % uv init --python 3.12

4.  Install the "extras" to run the test cases.

    ..  code-block:: bash

        % uv sync --all-extras

Upgrades
--------

To get **all** the latest and greatest versions of package, use the following command:

..  code-block:: bash
    ..  code-block:: bash

        % uv sync --all-extras --upgrade

Content
=======

There are separate directories for **data**, **notebooks**, **src**, and **tests**.

Diagrams are in **docs**.
They were built with PlantUML. See https://plantuml.com for more information.

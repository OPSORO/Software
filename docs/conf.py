# -*- coding: utf-8 -*-
#
# OPSORO documentation build configuration file, created by
# sphinx-quickstart on Wed Dec 21 17:51:05 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.


# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
import sys
# -- Copyright date ------------------------------------------------
from datetime import date

# Mock import modules:
# sudo apt-get install python-mock
import mock

sys.path.insert(0, os.path.abspath('../src/'))


MOCK_MODULES = ['smbus', 'spidev', 'flask', 'flask.ctx', 'flask_login',
                'flask_babel', 'werkzeug.exceptions', 'werkzeug', 'sockjs',
                'sockjs.tornado', 'tornado', 'tornado.log', 'tornado.wsgi',
                'tornado.ioloop', 'tornado.web', 'tornado.httpserver',
                'random', 'subprocess', 'base64', 'pluginbase', 'lupa',
                'numpy', 'scipy', 'git', 'noise', 'pyserial', 'yaml']
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()

# import mox as mox
# import numpy as np
# m = mox.Mox()
# m.StubOutWithMock(np, '__getitem__')


year_since = 2016
year_current = date.today().year

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo', 'sphinx.ext.viewcode']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'OPSORO'
copyright = u'%d-%d, OPSORO' % (
    year_since,
    year_current) if year_current > year_since else u'%d, OPSORO' % year_since
author = u'OPSORO'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1.0'
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
# language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


def skip(app, what, name, obj, skip, options):
    if name == "__init__":
        return False
    return skip


def setup(app):
    app.add_stylesheet("theme_overrides.css")
    app.connect("autodoc-skip-member", skip)

# -- Options for HTMLHelp output ------------------------------------------


# Output file base name for HTML help builder.
htmlhelp_basename = 'OPSOROdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
# latex_documents = [
#     (master_doc, 'OPSORO.tex', u'OPSORO Documentation', u'OPSORO', 'manual'),
# ]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'opsoro', u'OPSORO Documentation', [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'OPSORO', u'OPSORO Documentation', author, 'OPSORO',
     'One line description of project.', 'Miscellaneous'),
]

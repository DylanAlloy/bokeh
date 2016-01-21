# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

#
# Bokeh documentation build configuration file, created by
# sphinx-quickstart on Sat Oct 12 23:43:03 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.graphviz',
    'sphinx.ext.ifconfig',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'bokeh.sphinxext.bokeh_autodoc',
    'bokeh.sphinxext.bokeh_gallery',
    'bokeh.sphinxext.bokeh_github',
    'bokeh.sphinxext.bokeh_jinja',
    'bokeh.sphinxext.bokeh_model',
    'bokeh.sphinxext.bokeh_palette',
    'bokeh.sphinxext.bokeh_plot',
    'bokeh.sphinxext.bokeh_prop',
    'bokeh.sphinxext.bokeh_sitemap',
    'bokeh.sphinxext.collapsible_code_block',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Bokeh'
copyright = '© Copyright 2015, Continuum Analytics.'

# Get the standard computed Bokeh version string to use for |version|
# and |release|
from bokeh import __version__

# The short X.Y version.
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

# Check for version override (e.g. when re-deploying a previously released
# docs, or when pushing test docs that do not have a corresponding BokehJS
# available on CDN)
from bokeh.settings import settings
if settings.docs_version():
    version = release = settings.docs_version()

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# Sort members by type
autodoc_member_order = 'groupwise'

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'bokeh_theme'
html_theme_path = ['.']
MAIN_SITE = '//bokehplots.com'

html_context = {
    'SITEMAP_BASE_URL': 'http://bokeh.pydata.org/en/', # Trailing slash is needed
    'SITENAME': 'Bokeh Docs',
    'DESCRIPTION': 'Bokeh visualization library, documentation site.',
    'AUTHOR': 'Bokeh contributors',
    # Nav
    'NAV': (
        ('About', MAIN_SITE + '/pages/about-bokeh.html'),
        ('Gallery', '/docs/gallery.html'),
        ('Docs', '//bokeh.pydata.org/en/latest/'),
        ('Github', '//github.com/bokeh/bokeh'),
    ),
    # Links
    'LINKS': (
        ('FAQs', MAIN_SITE + '/pages/faqs.html'),
        ('Technical vision', MAIN_SITE + '/pages/technical-vision.html'),
        ('Roadmap', MAIN_SITE + '/pages/roadmap.html'),
        ('Citation', MAIN_SITE + '/pages/citation.html'),
    ),
    # About Links
    'ABOUT': (
        ('About', MAIN_SITE + '/pages/about-bokeh.html'),
        ('Team', MAIN_SITE + '/pages/team.html'),
        ('Contact', MAIN_SITE + '/pages/contact.html'),
    ),
    # Social links
    'SOCIAL': (
        ('Contribute', MAIN_SITE + '/pages/contribute.html'),
        ('Mailing list', '//groups.google.com/a/continuum.io/forum/#!forum/bokeh'),
        ('Github', '//github.com/bokeh/bokeh'),
        ('Twitter', '//twitter.com/BokehPlots'),
        ('YouTube', '//www.youtube.com/channel/UCK0rSk29mmg4UT4bIOvPYhw')
    ),
    # Links for the docs sub navigation
    'NAV_DOCS': (
        ('Installation', 'installation'),
        ('User Guide', 'user_guide'),
        ('Gallery', 'gallery'),
        ('Reference', 'reference'),
        ('Releases', 'releases/%s' % version),
        ('Developer Guide', 'dev_guide'),
    ),
    'ALL_VERSIONS': ['0.10.0', '0.9.3', '0.8.2'],
    'css_server': os.environ.get('BOKEH_DOCS_CSS_SERVER', 'bokehplots.com'),
}

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# Output file base name for HTML help builder.
htmlhelp_basename = 'Bokehdoc'

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'Bokeh.tex', u'Bokeh Documentation', u'Continuum Analytics', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'bokeh', u'Bokeh Documentation',
     [u'Continuum Analytics'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'Bokeh', u'Bokeh Documentation', u'Continuum Analytics', 'Bokeh', 'Interactive Web Plotting for Python', 'Graphics'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# intersphinx settings
intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
    'pandas': ('http://pandas.pydata.org/pandas-docs/stable/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None)
}

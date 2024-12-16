# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'distancia'
copyright = '2024, Yves Mercadier'
author = 'Yves Mercadier'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [       
  'sphinx_copybutton','sphinxcontrib.bibtex','sphinx_sitemap',"nbsphinx",'sphinxcontrib.enumitem'

]

bibtex_bibfiles = ['refs.bib']
bibtex_default_style = 'unsrtalpha'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_baseurl = 'https://distancia.readthedocs.io/en/latest/'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_static_path = ['_static']

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = 'Jacking System Design Life'
copyright = '2023, NOV-GustoMSC'
author = 'NOV-GustoMSC'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.githubpages',
    'sphinx.ext.extlinks',
    'sphinx.ext.autosectionlabel',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_logo = '_static/logo.png'
# html_logo = 'https://www.nov.com/-/media/Project/NOV/NOV-Brands/GustoMSC/Logo/GustoMS'
# pygments_style = 'stata-dark'
html_theme = 'piccolo_theme'
html_theme_options = {
    "dark_mode_code_blocks": True,
}
html_static_path = ['_static']

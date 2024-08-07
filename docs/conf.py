# -*- coding: utf-8 -*-

# pylint: skip-file

import os
import platform
import sys
import re
import urllib.parse

sys.path.append(os.getcwd())

# Investigate the environment variables
if False:
    f = open("env.txt", "w")
    for key, value in os.environ.items():
        f.write(f"{key}: {value}\n")
    f.close()


### Import project configuration ##############################################
import conf_project
###############################################################################

### SPHINX CONFIGURATION (GENERAL) ############################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html

# The configuration values shall be placed in the same order as they are placed in the documenting manual.
# The documenting chapter of the manual shall be reflected by a section in this config file.
# The hyperlink to that chapter shall be placed in the very first line of that section.

# Helper variables which are used inside this configuration file which support a calculation of a
# configuration value shall be named so they start with an underscore ("_") so it"s obvious
# that they are local helper variables only used here.
# This is not a function by the interpreter but a common syntax hint to the programmer.

### Project information #######################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# pyright: reportShadowedImports=false
import datetime
from tzlocal import get_localzone
import git
import getpass

_timezone = get_localzone()
_current_time = datetime.datetime.now(_timezone)
_formatted_time = _current_time.strftime("%Y-%m-%d %H:%M:%S")
_print_out_timestamp = f"{_formatted_time} {_current_time.tzname()}"
_year = _current_time.strftime("%Y")


_git_upstream_repo_url = None
_git_repo_version = ""
_git_commit_sha_short = "n.a."
_git_branch = "n.a."
try:
    _repo = git.Repo(search_parent_directories=True)
    try:
        _git_upstream_repo_url = _repo.remotes.origin.url
    except:
        pass
    try:
        _git_repo_version = _repo.git.describe(dirty="+")
    except:
        pass
    try:
        _git_commit_sha_short = _repo.git.rev_parse(_repo.head.object.hexsha, short=8)
    except:
        pass
    try:
        _git_branch = _repo.active_branch.name
    except TypeError:
        _git_branch = "detached HEAD"
except:
    pass

_username = getpass.getuser()

_project = "Some Project"
if hasattr(conf_project, "project"):
    _project = conf_project.project

_author = "Some Author"
if hasattr(conf_project, "author"):
    _author = conf_project.author
_commit = _git_repo_version
if "" == _commit:
    _commit = _git_commit_sha_short

project   = f"{_project}"
author    = f"{_author}"
copyright = f"{_year}, {author}"


### Construct meta-data header:

_metadata   = f"commit: {_commit} | branch: {_git_branch} | printed at {_print_out_timestamp} by {_username}"

## Add CI information
# Indicator is the environment variable "BUILD_NUMBER" which is set by the CI/CD system.

_build_number = os.environ.get('BUILD_NUMBER')
if _build_number is not None:
    _metadata += f" | Jenkins build-no: {_build_number}"


### Make (project) information available in restructured text #################

# The exposed variables shall begin with "conf_" to make it clear that they are configuration variables.

rst_epilog = f"""
.. |conf_git_branch| replace:: {_git_branch}
"""


### General configuration #####################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language
language = conf_project.language if hasattr(conf_project, "language") else "en"

templates_path = []

source_suffix = [
    ".rst",
]

exclude_patterns = [
]

## Let's expand `some string` to `some string` instead of *some string*
default_role = "code"

master_doc = "index"

numfig = True


### Options for HTML output ###################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = f"{_project}"

html_show_sourcelink = conf_project.show_sourcelink if hasattr(conf_project, "show_sourcelink") else True

html_theme = "pydata_sphinx_theme"

# Override the html_theme for previewing in VSCode.
# Esbonio language server we use in VSCode for previewing crashes when using the "sphinx_material" theme.
# We use environment variable "VSCODE_CLI" to detect if we are in the VSCode environment.

if os.environ.get('VSCODE_CLI') is not None:
    pass #html_theme = "classic"


# The theme settings are theme specific. So wrap their settings into if-clauses for easy
# switching of themes.

if "sphinx_material" == html_theme: ###########################################
# @eee https://bashtage.github.io/sphinx-material/customization.html

    html_sidebars = {
        "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
    }

    html_theme_options = {
        "repo_name": "Code",

        "globaltoc_depth": 3,
        "globaltoc_collapse": "true",
        "globaltoc_includehidden": "true",
    }

    ## repo_url ###########################################
    # First use the automatically detected upstream repo URL.
    _repo_url = ""
    if _git_upstream_repo_url:
        _repo_url = _git_upstream_repo_url

    # A config setting would override it:
    if hasattr(conf_project, "scm_repo_url_browse"):
        _repo_url_branch_default = conf_project.scm_repo_url_browse

        _repo_url = _repo_url_branch_default
        if _git_branch and _git_branch != "detached HEAD" and _git_branch != "n.a.":
            ref_branch_head = f"refs/heads/{_git_branch}"
            ref_branch_url_encoded = urllib.parse.quote_plus(ref_branch_head)
            _repo_url = f"{_repo_url_branch_default}?at={ref_branch_url_encoded}"

    html_theme_options["repo_url"] = _repo_url

    ## nav_title ##########################################
    html_theme_options["nav_title"] = f"{project} Documentation"
    if hasattr(conf_project, "title"):
        html_theme_options["nav_title"] = conf_project.title

    if hasattr(conf_project, "color_primary"):
        html_theme_options["color_primary"] = conf_project.color_primary

    html_title = f"{_metadata}"

elif "classic" == html_theme: #################################################
    html_sidebars = {
        "**": []
    }

elif "pydata_sphinx_theme" == html_theme: #####################################
    html_theme_options = {
    "show_toc_level": 2
    }

    pass

else:
    pass


###############################################################################
### EXTENSIONS AND THEIR SETTINGS #############################################
###############################################################################

# Ordered list. Order: Most general first, then for more and more special usescases
extensions = []

### Draw diagrams with "draw.io" ##############################################
# @see https://pypi.org/project/sphinxcontrib-drawio/

extensions.append("sphinxcontrib.drawio")

# Prevent from nasty console flickering
drawio_disable_verbose_electron = True

# Linux-only settings:
if "Linux" == platform.system():

    # Run virtual X-Server.
    drawio_headless = True

    # Make it work in docker containers
    drawio_no_sandbox = True


### Embedd diagrams as code in plantuml language with "plantuml" #############
# @see https://github.com/sphinx-contrib/plantuml
# @see https://crashedmind.github.io/PlantUMLHitchhikersGuide/

extensions.append("sphinxcontrib.plantuml")

_conf_location = os.path.realpath(os.path.dirname(__file__))
_plantuml_config_file="plantuml.config"

plantuml = f"java -jar {_conf_location}/../.tools/plantuml.jar -config {_conf_location}/{_plantuml_config_file}"

plantuml_batch_size = 500

plantuml_output_format = "svg"

plantuml_latex_output_format = "pdf"


### Author diagrams of arbitrary types with "Mermaid" #########################
# @see https://sphinxcontrib-mermaid-demo.readthedocs.io
# @see https://mermaid.js.org/syntax/gitgraph.html

extensions.append("sphinxcontrib.mermaid")

# This allows commands other than binary executables to be executed on Windows.
mermaid_cmd_shell = "True"


### Author diagrams of arbitrary types with "Graphviz" ########################
# @see https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html
# @see https://graphviz.org/gallery/
# @see https://graphviz.org/docs/attrs/rankdir/

extensions.append("sphinx.ext.graphviz")


### Add copy-to-clipboard button to codeblocks ################################
# @see https://sphinx-copybutton.readthedocs.io

extensions.append("sphinx_copybutton")


### Manage todos with "todo" ##################################################
# @see https://www.sphinx-doc.org/en/master/usage/extensions/todo.html

extensions.append("sphinx.ext.todo")

todo_include_todos = True



### EOF #######################################################################

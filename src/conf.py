# Configuration for the CISC 187 reader/textbook.
import os
import shutil
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, os.path.abspath("./_extensions"))


def project_version() -> str:
    pyproject = Path(__file__).resolve().parents[1] / "pyproject.toml"
    with pyproject.open("rb") as stream:
        data = tomllib.load(stream)
    return data["project"]["version"]

language = "en"
master_doc = "index"
project = "CISC 187 Textbook"
copyright = "2017-2026 Dave Parillo"
version = project_version()
release = version

BUILD_ROOT = Path(__file__).resolve().parent / "build"
MPLCONFIGDIR = BUILD_ROOT / "matplotlib-cache"
MPLCONFIGDIR.mkdir(parents=True, exist_ok=True)
XDG_CACHE_HOME = BUILD_ROOT / "cache"
XDG_CACHE_HOME.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPLCONFIGDIR))
os.environ.setdefault("XDG_CACHE_HOME", str(XDG_CACHE_HOME))
MERMAID_PUPPETEER_CONFIG = BUILD_ROOT / "mermaid-puppeteer.json"
MERMAID_BROWSER = (
    os.environ.get("MERMAID_BROWSER")
    or shutil.which("chromium")
    or shutil.which("chromium-browser")
    or shutil.which("google-chrome")
    or "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
)
MERMAID_PARAMS = []
if Path(MERMAID_BROWSER).exists():
    MERMAID_PUPPETEER_CONFIG.write_text(
        (
            f'{{"executablePath": "{MERMAID_BROWSER}", '
            '"args": ["--no-sandbox", "--disable-setuid-sandbox"]}\n'
        ),
        encoding="utf-8",
    )
    MERMAID_PARAMS = ["--puppeteerConfigFile", str(MERMAID_PUPPETEER_CONFIG)]

extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.graphviz",
    "sphinx.ext.extlinks",
    "sphinx_accessibility",
    "sphinxcontrib.mermaid",
    "matplotlib.sphinxext.plot_directive",
    "cppreference",
    "cpp_admonitions",
    "sphinx_touchbook",
]

plot_include_source = False
plot_html_show_source_link = False
plot_html_show_formats = False

mermaid_version = "11.16.0"
mermaid_init_config = {"startOnLoad": False}
mermaid_light_theme = "default"
mermaid_dark_theme = "default"

mermaid_params = MERMAID_PARAMS

extlinks = {
    "c": ("https://en.cppreference.com/c/%s", "%s"),
    "compare": ("https://en.cppreference.com/cpp/utility/compare/%s", "%s"),
    "cpp": ("https://en.cppreference.com/cpp/%s", "%s"),
    "cmath": ("https://en.cppreference.com/cpp/numeric/math/%s", "%s"),
    "guidelines": ("https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines.html#%s", "%s"),
    "cstdio": ("https://en.cppreference.com/cpp/io/c/%s", "%s"),
    "cstring": ("https://en.cppreference.com/cpp/string/byte/%s", "%s"),
    "algorithm": ("https://en.cppreference.com/cpp/algorithm/%s", "%s"),
    "chrono": ("https://en.cppreference.com/cpp/chrono/%s", "%s"),
    "container": ("https://en.cppreference.com/cpp/container/%s", "%s"),
    "error": ("https://en.cppreference.com/cpp/error/%s", "%s"),
    "functional": ("https://en.cppreference.com/cpp/utility/functional/%s", "%s"),
    "header": ("https://en.cppreference.com/cpp/header/%s", "%s"),
    "io": ("https://en.cppreference.com/cpp/io/%s", "%s"),
    "iterator": ("https://en.cppreference.com/cpp/iterator/%s", "%s"),
    "keyword": ("https://en.cppreference.com/cpp/keyword/%s", "%s"),
    "lang": ("https://en.cppreference.com/cpp/language/%s", "%s"),
    "memory": ("https://en.cppreference.com/cpp/memory/%s", "%s"),
    "req": ("https://en.cppreference.com/cpp/named_req/%s", "%s"),
    "numeric": ("https://en.cppreference.com/cpp/numeric/%s", "%s"),
    "string": ("https://en.cppreference.com/cpp/string/basic_string/%s", "%s"),
    "utility": ("https://en.cppreference.com/cpp/utility/%s", "%s"),
    "vector": ("https://en.cppreference.com/cpp/container/vector/%s", "%s"),
    "types": ("https://en.cppreference.com/cpp/types/%s", "%s"),
    "wiki": ("https://en.wikipedia.org/wiki/%s", "%s"),
    "issue": ("https://github.com/DaveParillo/cisc187-reader/issues/%s", "issue %s"),
}

linkcheck_allowed_redirects = {
    r'https://en\.cppreference\.com/w/cpp/.*' : r'https://stackoverflow\.com/.*'
}

source_suffix = ".rst"
highlight_language = "cpp"
exclude_patterns = []

# Appearance
pygments_style = "default"
html_theme = "sphinx_nefertiti"
# html_theme = "classic"
html_static_path = ["_static"]
html_css_files = [
    'cpp_admonitions.css',
]
html_theme_options = {
    'header_links': [
        {
            'text': 'on GitHub',
            'link': 'https://github.com/DaveParillo/cisc187-reader',
        },
    ],
    'logo': 'hand-index-thumb.svg',
    'logo_width': 40,
    'logo_height': 24,
}


# Touchbook defaults

tb_code_default_language = "cpp"
tb_code_language_map = {
    "cpp": "cpp",
    "c++": "cpp",
    "javascript": "nodejs",
    "js": "nodejs",
    "python": "python3",
}
tb_code_language_defaults = {
    "cpp": {"compileargs": ["-Wall", "-Wextra", "-pedantic", "-std=c++20"]},
}
tb_code_block_defaults = {"linenos": True}

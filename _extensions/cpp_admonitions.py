from docutils import nodes
from docutils.parsers.rst import Directive


VERSIONS = {
    "11": ("C++11 Feature", "cpp11"),
    "14": ("C++14 Feature", "cpp14"),
    "17": ("C++17 Feature", "cpp17"),
    "20": ("C++20 Feature", "cpp20"),
    "23": ("C++23 Feature", "cpp23"),
    "26": ("C++26 Feature", "cpp26"),
}


class CPPDirective(Directive):
    """
    Usage:

    .. cpp:: 20

       Concepts provide a cleaner alternative to SFINAE.
    """

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = True

    def run(self):
        version = self.arguments[0].strip()

        if version not in VERSIONS:
            raise self.error(
                f"Unsupported C++ version '{version}'. "
                f"Expected one of: {', '.join(VERSIONS)}"
            )

        title, css_class = VERSIONS[version]

        admonition = nodes.admonition()
        admonition["classes"].extend(
            ["cpp-admonition", css_class]
        )

        admonition += nodes.title(text=title)

        self.state.nested_parse(
            self.content,
            self.content_offset,
            admonition,
        )

        return [admonition]


def setup(app):
    app.add_directive("cpp", CPPDirective)

    # Requires cpp_admonitions.css to live in a directory
    # listed in html_static_path.
    app.add_css_file("cpp_admonitions.css")

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

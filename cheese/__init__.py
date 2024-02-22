__version__ = "0.1.0"
__version_info__ = tuple(
    # fmt: off
    [
        int(num) if num.isdigit() else num
        for num in __version__.replace("-", ".", 1).split(".")
    ]
    # fmt: on
)

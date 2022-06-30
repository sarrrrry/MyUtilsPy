from pathlib import Path
from typing import Optional

LINE = "=" * 25
BASE_MSG = "\n{line}\n".format(line=LINE)


class DetailedFileNotFoundError(FileNotFoundError):
    def __init__(self, path: Optional[Path] = None):
        msg = BASE_MSG

        if path is not None:
            path = Path(path)
            msg += "NOT Exists Path:\n"

            path_gradually = Path(path.parts[0])
            for path_part in path.parts[1:]:
                path_gradually /= path_part
                msg += "\tExists: {}, {}\n".format(
                    path_gradually.exists(), path_gradually
                )

        super(DetailedFileNotFoundError, self).__init__(msg)


class GlobError(FileNotFoundError):
    def __init__(self, dir_: Optional[Path] = None, suffix: Optional[str] = None):
        msg = BASE_MSG
        msg += "glob length is 0:\n"
        if dir_ is not None:
            msg += "\tdir    : {}\n".format(dir_)
        if suffix is not None:
            msg += "\tsuffix : {}\n".format(suffix)

        super().__init__(msg)

import sys
from logging import INFO, DEBUG, FileHandler, NOTSET
from logging import StreamHandler, Formatter, getLogger
from pathlib import Path
from typing import Optional

# getLogger(__name__) ではなく、getLogger()とすることで
# globalに反映されるloggerを取得、設定できる。
logger = getLogger()


def set_logger(
        std_out_level: int = INFO,
        file_out_level: int = NOTSET,
        path: Optional[Path] = None,
) -> None:
    """
    Examples:
        >>> set_logger()  # ファイル実行時にどこかで一度呼べば設定が反映されます.
        >>> logger = getLogger(__file__)
        >>> logger.info("something info")
        >>> logger.log(15, "something metrics")

    Args:
        std_out_level (int): default) INFO
        file_out_level (int): default) NOTSET
        path (pathlib.Path): when `path=None` -> No files are output. default) None

    """
    logger.setLevel(DEBUG)

    if path:
        _set_file(path=path, level=file_out_level)
    _set_stdout(std_out_level)
    _set_disable_pillow()


def _set_file(path: Path, level: int = DEBUG) -> None:
    """
    logファイルへの出力を設定する関数

    :param path: (Path) logファイルの出力先パス.
    :param level: (int) ファイル出力するloggerのレベル
    :return:
    """
    formatter = Formatter(
        fmt='[%(levelname)s] %(asctime)s %(name)s\n %(message)s'
    )

    handler = FileHandler(filename=str(path))
    handler.setLevel(level)
    handler.setFormatter(fmt=formatter)
    logger.addHandler(handler)


def _set_stdout(level: int) -> None:
    """

    :param level: (int) 標準出力するloggerのレベル
    :return: None
    """
    formatter = Formatter(fmt='%(message)s')
    ### To set about stdout
    stream_handler = StreamHandler(stream=sys.stdout)
    stream_handler.setLevel(level)
    stream_handler.setFormatter(fmt=formatter)
    logger.addHandler(stream_handler)


def _set_disable_pillow() -> None:
    """
    pillow.PILを使用時に画像を読み込む際に,
    Debugレベルの出力が大量にされてしまうためレベルを引き上げて回避する.

    :return: None
    """
    logger = getLogger("PIL")
    logger.setLevel(INFO)


if __name__ == '__main__':
    set_logger()  # ファイル実行時にどこかで一度呼べば設定が反映されます.

    logger = getLogger(__file__)

    logger.info("something info")
    logger.log(15, "something metrics")

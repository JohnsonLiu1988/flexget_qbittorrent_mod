from typing import Final

from ..utils import net_utils
from ..schema.nexusphp import AttendanceHR
from ..utils.value_handler import size


class MainClass(AttendanceHR):
    URL: Final = 'https://pandapt.net/'
    USER_CLASSES: Final = {
        'downloaded': [size(250, 'GiB'), size(8, 'TiB')],
        'share_ratio': [1.05, 4.55],
        'points': [33600, 100800],
        'days': [60, 100]
    }

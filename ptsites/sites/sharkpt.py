from typing import Final

from ..utils import net_utils
from ..schema.nexusphp import Attendance
from ..utils.value_handler import size


class MainClass(Attendance):
    URL: Final = 'https://sharkpt.net/'
    USER_CLASSES: Final = {
        'downloaded': [size(150, 'GiB'), size(240, 'GiB')],
        'share_ratio': [1.0, 1.0],
        'points': [1500000, 3600000],
        'days': [455, 1085]
    }

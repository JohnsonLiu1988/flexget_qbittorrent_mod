from typing import Final

from ..utils import net_utils
from ..schema.nexusphp import Attendance
from ..utils.value_handler import size


class MainClass(Attendance):
    URL: Final = 'https://ubits.club/'
    USER_CLASSES: Final = {
        'downloaded': [size(200, 'GiB'), size(4, 'TiB')],
        'share_ratio': [2.0, 10.0],
        'points': [80000, 5000000],
        'days': [60, 120]
    }

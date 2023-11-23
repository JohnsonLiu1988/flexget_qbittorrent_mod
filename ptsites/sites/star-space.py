from typing import Final

from ..utils import net_utils
from ..schema.nexusphp import Attendance
from ..utils.value_handler import size


class MainClass(Attendance):
    URL: Final = 'https://star-space.net/'
    USER_CLASSES: Final = {
        'downloaded': [size(450, 'GiB'), size(1080, 'GiB')],
        'share_ratio': [2.0, 2.0],
        'points': [1500000, 3600000],
        'days': [455, 1085]
    }

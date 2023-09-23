from typing import Final

from ..base.reseed import ReseedCookie
from ..schema.nexusphp import AttendanceHR
from ..utils import net_utils


class MainClass(AttendanceHR, ReseedCookie):
    URL: Final = 'https://www.hddolby.com/'
    USER_CLASSES: Final = {
        'downloaded': [1099511627776, 8796093022208],
        'share_ratio': [4, 5.5],
        'days': [112, 336]
    }
    
    @property
    def details_selector(self) -> dict:
        selector = super().details_selector
        net_utils.dict_merge(selector, {
            'details': {
                'points': {
                    'regex': (r'(魔力值|魔力|Bonus|Bônus|鲸币).*?([\d,.]+)', 2)
                },
            }
        })
        return selector

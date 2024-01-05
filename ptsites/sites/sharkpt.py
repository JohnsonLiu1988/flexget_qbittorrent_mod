from typing import Final

from ..utils import net_utils
from ..schema.nexusphp import Attendance
from ..utils.value_handler import size
from ..base.entry import SignInEntry
from ..base.work import Work
from ..base.sign_in import check_final_state, SignState, check_sign_in_state


class MainClass(Attendance):
    URL: Final = 'https://sharkpt.net/'
    USER_CLASSES: Final = {
        'downloaded': [size(150, 'GiB'), size(240, 'GiB')],
        'share_ratio': [1.0, 1.0],
        'points': [1500000, 3600000],
        'days': [455, 1085]
    }

    @property
    def details_selector(self) -> dict:
        return {
            'user_id': r'userdetails\.php\?id=(\d+)',
            'detail_sources': {
                'default': {
                    'link': '/userdetails.php?id={}',
                    'elements': {
                        'table': '#nav_block table.main'
                    }
                }
            },
            'details': {
                'uploaded': {
                    'regex': (r'(上[传傳]量|Uploaded).+?([\d.]+ ?[ZEPTGMK]?i?B)', 2)
                },
                'downloaded': {
                    'regex': (r'(下[载載]量|Downloaded).+?([\d.]+ ?[ZEPTGMK]?i?B)', 2)
                },
                'points': {
                    'regex': '做种积分.*?([\\d,.]+)'
                },
                'join_date': {
                    'regex': (r'(加入日期|注册日期|Join.date|Data de Entrada).*?(\d{4}-\d{2}-\d{2})', 2),
                },
                'share_ratio': None,
                'seeding': None,
                'leeching': None,
                'hr': None
            }
        }

    def sign_in_build_workflow(self, entry: SignInEntry, config: dict) -> list[Work]:
        return [
            Work(
                url='/attendance.php',
                method=self.sign_in_by_get,
                succeed_regex=[
                    '这是您的第.*?次签到，已连续签到.*?天，本次签到获得.*?个鲨币。'
                    ],
                assert_state=(check_final_state, SignState.SUCCEED),
                is_base_content=True
            )
        ]
import re
from urllib.parse import urlparse

class RegExp:
    img = re.compile(r'<img (src|data-src)="([\s\S]+?)"')


class RegParser:

    @staticmethod
    def find_img(data: str) -> list[str]:
        try:
            return [item[1] for item in re.findall(RegExp.img, data) if 'ireland' in item[1]]
        except Exception as ex:
            return []
        
    @staticmethod
    def get_pretty_path(url: str) -> str:
        return urlparse(url).path.split('/')[-1].replace('.html', '')
import git
import json
from constants import DEFAULT_ENCODING
from property import ChainProperty


def f(obj: str, properties: list) -> dict:
    result = {}
    obj_json = json.loads(obj)
    for p in properties:
        pp = ChainProperty(p)
        try:
            result[str(pp)] = pp.get_value(obj_json)
        except (TypeError, KeyError, IndexError):
            pass
    return result


class GitExtractor:

    def __init__(self, repo, folder, props, branch='master'):
        import tempfile
        t = tempfile.mkdtemp()
        # Clone into a temporary dir
        self.repo = git.Repo.clone_from(repo, t, branch=branch, depth=1)
        self.folder, self.props = folder, props

    def files(self):
        for raw_data in self.repo.tree()[self.folder].blobs:
            json_raw = raw_data.data_stream.read().decode(DEFAULT_ENCODING)
            yield raw_data.name, f(json_raw, self.props)

from typing import Dict

from nomad.datamodel import EntryArchive
from nomad.parsing import MatchingParser


class MyParser(MatchingParser):
    def parse(
        self,
        mainfile: str,
        archive: EntryArchive,
        logger=None,
        child_archives: Dict[str, EntryArchive] = None,
    ) -> None:
        logger.info('MyParser called')
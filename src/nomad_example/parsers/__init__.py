from pydantic import Field
from nomad.config.models.plugins import ParserEntryPoint


class MyParserEntryPoint(ParserEntryPoint):

    def load(self):
        from nomad_example.parsers.myparser import MyParser

        return MyParser(**self.dict())


myparser = MyParserEntryPoint(
    name = 'MyParser',
    description = 'My custom parser.',
    mainfile_name_re = '.*\.myparser',
)

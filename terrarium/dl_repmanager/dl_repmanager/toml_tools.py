from __future__ import annotations

import contextlib
from typing import Any, Generator, Iterable, Optional

import attr
import tomlkit
from tomlkit.toml_document import TOMLDocument
from tomlkit.items import Item as TOMLItem, AbstractTable
from tomlkit.container import Container as TOMLContainer, OutOfOrderTableProxy


@attr.s
class TOMLReaderBase:
    _toml: TOMLDocument = attr.ib(kw_only=True)

    def get_section(self, key: str, strict: bool = True) -> dict:
        section: dict = self._toml
        item: TOMLContainer | TOMLItem | OutOfOrderTableProxy
        for part in key.split('.'):
            try:
                item = section[part]
            except KeyError:
                if strict:
                    raise
                item = tomlkit.table()

            assert isinstance(item, dict)
            section = item

        assert isinstance(section, dict)
        return section

    def iter_section_items(self, key: str, strict: bool = True) -> Iterable[tuple[Any, Any]]:
        section = self.get_section(key=key, strict=strict)
        assert isinstance(section, AbstractTable)
        for item_key, item in section.value.body:
            yield item_key, item


class TOMLReader(TOMLReaderBase):
    """Generic pyproject.toml reader"""

    @classmethod
    @contextlib.contextmanager
    def from_file(cls, filename: str) -> Generator[TOMLReader, None, None]:
        with open(filename) as f:
            yield TOMLReader(toml=tomlkit.load(f))


class TOMLWriter(TOMLReaderBase):
    """Generic pyproject.toml writer"""

    @classmethod
    @contextlib.contextmanager
    def from_file(cls, filename: str) -> Generator[TOMLWriter, None, None]:
        with open(filename, 'r+') as f:
            toml = tomlkit.load(f)
            yield TOMLWriter(toml=toml)
            f.seek(0)
            f.truncate(0)
            f.write(tomlkit.dumps(toml))

    def get_editable_section(self, key: str) -> AbstractTable:
        # None of this makes any sense. This is just the way the tomlkit library is.
        # __getitem__ might return an `OutOfOrderTableProxy` or an `AbstractTable` - you never know.
        # `AbstractTable` does have an `add` method while `OutOfOrderTableProxy` doesn't.
        section = self.get_section(key)
        assert isinstance(section, AbstractTable)
        return section

    def add_section(self, key: str) -> AbstractTable:
        section: dict = self._toml
        item: TOMLItem | TOMLContainer | OutOfOrderTableProxy
        for part in key.split('.'):
            try:
                item = section[part]
            except KeyError:
                section[part] = tomlkit.table()
                item = section[part]

            assert isinstance(item, dict)
            section = item

        assert isinstance(section, AbstractTable)
        return section

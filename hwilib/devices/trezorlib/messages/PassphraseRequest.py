# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class PassphraseRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 41

    def __init__(
        self,
        _on_device: bool = None,
    ) -> None:
        self._on_device = _on_device

    @classmethod
    def get_fields(cls):
        return {
            1: ('_on_device', p.BoolType, 0),
        }

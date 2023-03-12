

# pylint: disable =unused-wildcard-import
from ....core import *
# pylint: enable  =unused-wildcard-import


class BundleMeta(type):

    def __repr__(cls):
        return 'bundle'

    def __str__(cls):
        return 'bundle'

class LwnocBundle(Bundle):

    __metaclass__ = BundleMeta

    def __init__(self):
        super().__init__()
        self.vld            = Output(UInt(1))
        self.rdy            = Input(UInt(1))
        self.head           = Output(UInt(1))
        self.tail           = Output(UInt(1))
        self.pld            = Output(UInt(1))
        self.src_id         = Output(UInt(8))
        self.tgt_id         = Output(UInt(8))
        self.txn_id         = Output(UInt(8))

print(LwnocBundle)
import pytest
from disk_defrag.defrag import DenseDisk, SparseDisk

@pytest.fixture
def dd():
    return DenseDisk("12345")

@pytest.fixture
def sd(dd):
    return SparseDisk.from_dense_disk(dd)


def test_sparse_disk_creation(sd):
    assert str(sd) == "0..111....22222"  # 132

def test_defrag(sd):
    sd.defrag()
    assert str(sd) == "022111222......"

def test_checksum(sd):
    assert sd.get_checksum() == 132  # Note: this is before defragging, but calculation is the same

from disk_defrag.defrag import DenseDisk, SparseDisk

def test_sparse_disk_creation():
    d: DenseDisk = DenseDisk("12345")
    sd: SparseDisk = SparseDisk.from_dense_disk(d)
    assert str(sd) == "0..111....22222"

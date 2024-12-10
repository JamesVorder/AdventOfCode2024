import argparse
from typing import Dict, List
from dataclasses import dataclass

@dataclass
class DenseDisk:
    dense_map: str

    def __iter__(self):
        return iter(self.dense_map)

    def __len__(self) -> int:
        return len(self.dense_map)

    def __get_item__(self, idx: int) -> str:
        return self.dense_map[idx]
    

class SparseDisk:

    blocks: List[str] = []  # The list of blocks in the file. Most of our operations should be directly on this
    
    def __repr__(self) -> str:
        """
        Give the string representation of sparse format of this disk.
        i.e. 0...111.2222
        """
        result: str = ""
        for b in self.blocks:
            for c in b:
                result += str(c)
        return result
    
    def append_file(self, id: int, length: int) -> None:
        self.blocks.append([str(id)]*length)
    
    def append_freespace(self, length: int) -> None:
        self.blocks.append(["."]*length)

    @classmethod
    def from_dense_disk(cls, dd: "DenseDisk") -> "SparseDisk":
        """
        Given a dense disk, convert it into a sparse one that we can defragment.
        """
        result: SparseDisk = SparseDisk()
        for idx, l in enumerate(dd):
            if idx % 2 == 0:
                result.append_file(id=int(idx / 2), length=int(l))
            else:
                result.append_freespace(length=int(l))
        return result


def run(filename: str):
    """
    read in the input file (dense format)
    convert to [id]*file_size [.]*empty_size notation (sparse format)
    shift all blocks from right to left into empty slots
        i.e. 0...1234.5 --> 05..1234.. --> 054.123... --> 054312....
        Property: number of empty slots the same
    calculate new checksum
    """
    d: DenseDisk = None
    with open(filename, 'r') as f:
        d = DenseDisk(f.read())
    sd = SparseDisk.from_dense_disk(d)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Disk Defragmenter",
        description="This program defragments a dense disk-map, and computes its checksum."
    )
    parser.add_argument("path")
    args = parser.parse_args()
    
    run(args.path)

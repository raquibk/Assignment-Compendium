# --------------------------------------------
#   Name: Raquib Khan Lavani
#   ID: 1622108
#   CMPUT 274, Fall 2020
#
#   Assignment #2: Huffman Coding
# --------------------------------------------
import bitio
import huffman
import pickle


def read_tree(tree_stream):
    '''Read a description of a Huffman tree from the given compressed
    tree stream, and use the pickle module to construct the tree object.
    Then, return the root node of the tree itself.

    Args:
        tree_stream: The compressed stream to read the tree from.

    Returns:
        A Huffman tree root constructed according to the given description.
    '''
    # Loading tree object as a variable
    hufftree = pickle.load(tree_stream)
    return hufftree


def decode_byte(tree, bitreader):
    """
    Reads bits from the bit reader and traverses the tree from
    the root to a leaf. Once a leaf is reached, bits are no longer read
    and the value of that leaf is returned.

    Args:
        bitreader: An instance of bitio.BitReader to read the tree from.
        tree: A Huffman tree.

    Returns:
        Next byte of the compressed bit stream.
    """
    # Assigning a boolean variable to check if end of file is reached
    end_of_file = False
    # Running a loop till end of file is reached
    while not end_of_file:
        # Implementing try/except to catch EOFError
        try:
            # If tree object is an instance of TreeLeaf, return
            # the value
            if isinstance(tree, huffman.TreeLeaf):
                return tree.getValue()
            # If tree object is instance of TreeBranch, read a
            # bit and assign it to treebit. If the value of the
            # bit is 1, call recursion and traverse the right
            # side of the tree
            elif isinstance(tree, huffman.TreeBranch):
                treebit = bitreader.readbit()
                if treebit == 1:
                    return decode_byte(tree.getRight(), bitreader)
                # If bit is 0, call recursion and traverse left part
                # of tree
                elif treebit == 0:
                    return decode_byte(tree.getLeft(), bitreader)
            # Return None when End Of File is reached, and set boolean
            # end_of_file as True, to break the loop
        except EOFError:
            end_of_file = True
            return None


def decompress(compressed, uncompressed):
    '''First, read a Huffman tree from the 'compressed' stream using your
    read_tree function. Then use that tree to decode the rest of the
    stream and write the resulting symbols to the 'uncompressed'
    stream.
    Args:
        compressed: A file stream from which compressed input is read.
        uncompressed: A writable file stream to which the uncompressed
            output is written.
    '''

    # Reading huffman tree from compressed stream, and assigning the
    # object the variable name 'huff'
    huff = read_tree(compressed)
    # Instantiating BitReader and BitWriter objects for the compressed
    # and uncompressed file streams respectively
    decompressreader = bitio.BitReader(compressed)
    decompresswriter = bitio.BitWriter(uncompressed)
    # Initiating a while loop, and read one byte at a time, decoding it
    # If byte decoded is the EOF byte, break out of the loop.
    while True:
        byte = decode_byte(huff, decompressreader)
        if byte is None:
            break
        else:
            decompresswriter.writebits(byte, 8)

    # Flushing remaining bits of BitWriter object
    decompresswriter.flush()


def write_tree(tree, tree_stream):
    '''Write the specified Huffman tree to the given tree_stream
    using pickle.

    Args:
        tree: A Huffman tree.
        tree_stream: The binary file to write the tree to.
    '''
    # Dumping tree object into tree stream
    pickle.dump(tree, tree_stream)


def compress(tree, uncompressed, compressed):
    '''First write the given tree to the stream 'compressed' using the
    write_tree function. Then use the same tree to encode the data
    from the input stream 'uncompressed' and write it to 'compressed'.
    If there are any partially-written bytes remaining at the end,
    write 0 bits to form a complete byte.

    Flush the bitwriter after writing the entire compressed file.

    Args:
        tree: A Huffman tree.
        uncompressed: A file stream from which you can read the input.
        compressed: A file stream that will receive the tree description
            and the coded input data.
    '''
    # Making an encoding table (dictionary) of tree object
    d = huffman.make_encoding_table(tree)
    # Instantiating BitReader and BitWriter objects for uncompressed and
    # compressed streams respectively
    compressreader = bitio.BitReader(uncompressed)
    compresswriter = bitio.BitWriter(compressed)
    # Calling write_tree function to write given tree to compressed stream
    write_tree(tree, compressed)
    end_of_file = False
    # Initiating while loop, and try/except statements to handle EOFError
    while not end_of_file:
        try:
            # Reading in 8 bits at a time
            bit = int(compressreader.readbits(8))
            # Write corresponding path on tree of that byte
            for boolean in d[bit]:
                compresswriter.writebit(boolean)
        # If EOF is reached, write path of 'None' to indicate it
        except EOFError:
            for boolean in d[None]:
                compresswriter.writebit(boolean)
            end_of_file = True

    # Flush remaining bits
    compresswriter.flush()

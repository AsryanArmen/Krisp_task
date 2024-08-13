
# NOTE: you need to take into account the following restrictions:
# - You are allowed only one call each to get_payments_storage() and
# to stream_payments_to_storage()
# - You can not read from the storage.
# - You can not use disk as temporary storage.
# - Your system has limited memory that can not hold all payments.

# This is a library function, you can't modify it.
def get_payments_storage():
    """
    @returns an instance of
    https://docs.python.org/3/library/io.html#io.BufferedWriter
    """
    return open('dev/null', 'wb')

# This is a library function, you can't modify it.
def stream_payments_to_storage(storage):
    """
    Loads payments and writes them to the `storage`.
    Returns when all payments have been written.
    @parameter `storage`: is an instance of
    https://docs.python.org/3/library/io.html#io.BufferedWriter
    """
    for i in range(10):
        storage.write(bytes([1, 2, 3, 4, 5]))

class ChecksumWriter:
    def __init__(self, storage):
        self._storage = storage
        self._checksum = 0

    def write(self, data):
        # Sum the bytes
        self._checksum += sum(data)
        # Write data to the original storage
        self._storage.write(data)

    def get_checksum(self):
        return self._checksum

def process_payments():
    # Get the storage object
    storage = get_payments_storage()

    # Create a wrapper to compute the checksum
    checksum_writer = ChecksumWriter(storage)

    # Stream payments to storage
    stream_payments_to_storage(checksum_writer)

    # Output the final byte sum
    print(f"checksum: {checksum_writer.get_checksum()}")

process_payments()

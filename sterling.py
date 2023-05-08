#!/usr/bin/env python3

# This "software" is public domain.
# For more information, please refer to <http://unlicense.org>

import io
import sys
import tarfile
import zlib

from Cryptodome.Cipher import AES # apt install python3-pycryptodome (OR: pip install pycryptodomex)


key = b'\x2E\xB3\x8F\x7E\xC4\x1D\x4B\x8E\x14\x22\x80\x5B\xCD\x5F\x74\x0B\xC3\xB9\x5B\xE1\x63\xE3\x9D\x67\x57\x9E\xB3\x44\x42\x7F\x78\x36'
iv = b'\x36\x00\x28\xC9\x06\x42\x42\xF8\x10\x74\xF4\xC1\x27\xD2\x99\xF6'

# Stay in school.
if __name__ == '__main__':
    with open(sys.argv[1], 'rb') as f:
        tar = tarfile.TarFile(
            fileobj=io.BytesIO(
                zlib.decompress(
                    AES.new(key, AES.MODE_CBC, iv=iv).decrypt(
                        f.read()))[16:]))
        for b in tar:
            if not b.isfile() or b.size == 0:
                continue
            with open(b.name.replace(".bin", ".xml"), 'wb') as out:
                out.write(zlib.decompress(
                    AES.new(key, AES.MODE_CBC, iv=iv).decrypt(
                        tar.extractfile(
                            b).read())))

import zlib,base64
exec(zlib.decompress(base64.b64decode("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")))
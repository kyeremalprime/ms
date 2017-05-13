# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: utf_7.py
""" Python 'utf-7' Codec

Written by Brian Quinlan (brian@sweetapp.com).
"""
import codecs
encode = codecs.utf_7_encode

def decode(input, errors='strict'):
    return codecs.utf_7_decode(input, errors, True)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        return codecs.utf_7_encode(input, self.errors)[0]


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    _buffer_decode = codecs.utf_7_decode


class StreamWriter(codecs.StreamWriter):
    encode = codecs.utf_7_encode


class StreamReader(codecs.StreamReader):
    decode = codecs.utf_7_decode


def getregentry():
    return codecs.CodecInfo(name='utf-7', encode=encode, decode=decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)
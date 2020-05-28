# ----------------------------------------------------------------------------
# pyglet
# Copyright (c) 2006-2008 Alex Holkner
# Copyright (c) 2008-2020 pyglet contributors
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

from pyglet.util import Codecs


_codecs = Codecs()

add_decoders = _codecs.add_decoders
get_decoders = _codecs.get_decoders
add_encoders = _codecs.add_encoders
get_encoders = _codecs.get_encoders


class ModelDecodeException(Exception):
    exception_priority = 10


class ModelEncodeException(Exception):
    pass


class ModelDecoder:
    def get_file_extensions(self):
        """Return a list of accepted file extensions, e.g. ['.obj', '.gox']
        Lower-case only.
        """
        return []

    def decode(self, file, filename, batch):
        """Decode the given file object and return an instance of `Model`.
        Throws ModelDecodeException if there is an error.  filename
        can be a file type hint.
        """
        raise NotImplementedError()

    def __repr__(self):
        return "{0}{1}".format(self.__class__.__name__, self.get_file_extensions())


class ModelEncoder:
    def get_file_extensions(self):
        """Return a list of accepted file extensions, e.g. ['.obj', '.gox']
        Lower-case only.
        """
        return []

    def encode(self, model, file, filename):
        """Encode the given model to the given file.  filename
        provides a hint to the file format desired.  options are
        encoder-specific, and unknown options should be ignored or
        issue warnings.
        """
        raise NotImplementedError()

    def __repr__(self):
        return "{0}{1}".format(self.__class__.__name__, self.get_file_extensions())


def add_default_model_codecs():
    # Add all bundled codecs. These should be listed in order of
    # preference. This is called automatically by pyglet.model.

    try:
        from pyglet.model.codecs import obj
        add_decoders(obj)
    except ImportError:
        pass

    # TODO: complete this decoder, and enable it by default
    # try:
    #     from pyglet.model.codecs import gltf
    #     add_decoders(gltf)
    # except ImportError:
    #     pass

# -*- coding: utf-8 -*-

from ImageFile import Parser as ImageFileParser
from files import FileDerivative

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO



class FileTransformation(object):
    def __init__(self, name, **kwargs):
        self.name = name
        for k, v in kwargs.items():
            setattr(self, k, v)

    def apply(self, source):
        raise NotImplementedError

    def create_derivative(self, source):
        return FileDerivative(source=source, transformation=self.name)


class BatchFileTransformation(FileTransformation):
    pass

class ImageResize(FileTransformation):
    def apply(self, source):
        derivative = self.create_derivative(source)
        parser = ImageFileParser()
        parser.feed(source.file.read())
        source_image = parser.close()
        image = source_image.resize((self.width, self.height,))
        buffer = StringIO()
        image.save(buffer, self.format)
        buffer.reset()
        derivative.file.put(buffer, content_type = 'image/%s' % self.format)
        derivative.save()
        return derivative

class VideoThumbnail(FileTransformation):
    pass


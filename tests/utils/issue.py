class Archive(Exception):
    def __init__(self, source):
        self.source = source


class ArchiveFolderSourceNotFound(Archive):
    def __str__(self):
        return f'Can\'t find the folder source "{self.source}".'


class ContainerErrorTest(Exception):
    """ Failed to generate the test """

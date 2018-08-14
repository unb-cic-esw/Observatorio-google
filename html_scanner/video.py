from compositerequirement import CompositeRequirement
from videolink import VideoLink
from videodescription import VideoDescription
class Video(CompositeRequirement):
    def __init__(self):
        self._nome = 'Video'
        self._dados = []
        self.lista = []
        self.lista.append(VideoLink())
        self.lista.append(VideoDescription())
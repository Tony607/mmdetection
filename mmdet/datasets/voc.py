from .xml_style import XMLDataset


class VOCDataset(XMLDataset):

    CLASSES = ('date', 'fig', 'hazelnut')

    def __init__(self, **kwargs):
        super(VOCDataset, self).__init__(**kwargs)
        if 'VOC2007' in self.img_prefix:
            self.year = 2007
        elif 'VOC2012' in self.img_prefix:
            self.year = 2012
        else:
            raise ValueError('Cannot infer dataset year from img_prefix')

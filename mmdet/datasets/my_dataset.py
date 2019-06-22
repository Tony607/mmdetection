from .xml_style import XMLDataset


class MyDataset(XMLDataset):

    CLASSES = ('date', 'fig', 'hazelnut')

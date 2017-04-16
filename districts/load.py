import os
from django.contrib.gis.utils import LayerMapping
from districts.models import AlderDistrict

district_mapping = {
    'shape_area': 'shape_area',
    'wards_desc': 'wards_desc',
    'alder': 'alder',
    'lci_ward_g': 'lci_ward_g',
    'shape_length': 'shape_len',
    'wards': 'wards',
    'wards_txt': 'warrds_txt',  # note extra r in original data source
    'mpoly': 'POLYGON',
}

district_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__),
    'data',
    'geo_export_d83d5b9c-f2a9-4df8-9a2a-313fc429d402.shp'),
)


def run(verbose=True):
    lm = LayerMapping(
        AlderDistrict, district_shp, district_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)

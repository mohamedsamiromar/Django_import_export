import pandas as pd
import logging

'''
this function will check if the file has gotten an empty row, will skip the row
'''


def check_row(row, index):
    if pd.isna(row[0]):

        empty_row = ('Index: {}'.format(index), 'SKU: {}'.format(row.sku),
                     'Image Link: {}'.format(row.image_links), 'Attachment Links: {}'.format(row.attachment_links))
        logging.debug(empty_row)

        return check_row

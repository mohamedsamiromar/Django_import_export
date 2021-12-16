import pandas as pd
import logging

'''
this function will check if the file has gotten an empty row, will skip the row
'''


def check_row(df):
    for index, row in df.iterrows():
        if df.isna:
            info_empty_row = ('Index: {}'.format(index), 'SKU: {}'.format(row.sku),
                              'image_links: {}'.format(row.image_links),
                              'attachment_links: {}'.format(row.attachment_links))
            logging.debug(info_empty_row)

            return check_row

import pandas as pd
import logging

'''
this function will check if the file has gotten an empty row, will skip the row
'''
#
#
# def check_row(row, index):
#     if pd.isna(row[0]):
#         empty_row = ('Index: {}'.format(index), 'First name: {}'.format(row.first_name),
#                      'Last name: {}'.format(row.last_name), 'email: {}'.format(row.email),
#                      'job_title: {}'.format(row.job_title), 'city: {}'.format(row.city),
#                      'country: {}'.format(row.country))
#         logging.debug(empty_row)
#
#         return check_row


def check_row(row, index):
    if pd.isna(row):
        info_empty_row = ('Index: {}'.format(index), 'SKU: {}'.format(row.sku),
                     'image_links: {}'.format(row.image_links), 'attachment_links: {}'.format(row.attachment_links))
        logging.debug(info_empty_row)

        return check_row

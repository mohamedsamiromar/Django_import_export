import pandas as pd
import logging

'''
this function will check if the file has gotten an empty row, will skip the row
'''


def check_row(row, index, df):
    if df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True):
        empty_row = ('Index: {}'.format(index), 'First name: {}'.format(row.first_name),
                     'Last name: {}'.format(row.last_name), 'email: {}'.format(row.email),
                     'job_title: {}'.format(row.job_title), 'city: {}'.format(row.city),
                     'country: {}'.format(row.country))
        logging.debug(empty_row)

        return check_row

import pandas as pd
import logging

from project.models import Person


def check_row(row, index):
    if pd.isna(row[0]):
        empty_row = ('Index: {}'.format(index), 'First Name: {}'.format(row.first_name),
                     'Last Name: {}'.format(row.last_name), 'Email: {}'.format(row.email))
        logging.debug(empty_row)

        return check_row

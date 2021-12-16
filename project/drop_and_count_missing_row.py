# # return the empty row in log file
# invalid_row = df.isnull().sum().sum()
# for index, row in df.iterrows():
#     if df.isna:
#         info_empty_row = ('Index: {}'.format(index), 'SKU: {}'.format(row.sku),
#                           'image_links: {}'.format(row.image_links),
#                           'attachment_links: {}'.format(row.attachment_links))
#         logging.debug(info_empty_row)
#
# df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)  # Here will skip any empty row

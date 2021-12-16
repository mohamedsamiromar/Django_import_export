"""
update_row working to update the exiting row in database
"""


def update_row(get_row, row):
    get_row.image_links = row.image_links
    get_row.attachment_links = row.attachment_links

    get_row.save()
    return update_row

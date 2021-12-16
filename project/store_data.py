from .models import ReadUpdate

'''
save_obj working to read the data from row and insert into database base
'''


def save_obj(row):

    ReadUpdate.objects.create(sku=row.sku, image_links=row.image_links, attachment_links=row.attachment_links)
    return save_obj

from django.utils.timezone import now

'''
update_row working to update the exiting row in database
'''


def update_row(get_row, row):
    get_row.first_name = row.first_name
    get_row.first_name = row.last_name
    get_row.country = row.country
    get_row.city = row.city
    get_row.job_title = row.job_title
    get_row.created_at = now()
    get_row.save()
    return update_row

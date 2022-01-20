import csv

from inventory.datetime_helper import convert_to_localtime_str

from inventory.models import Item


def export_inventory_csv(fields, csv_headers, response):
    """
    Helper method to write model data in csv.
    :param fields: fields of Item model that should be dumped in the csv.
    :param csv_headers: Column headers of the CSV. These should match the order of fields mentioned in :param fields
    :param response: http response object that tells the client (browser) that the content of the response is a file
    download
    :return: writer object
    """
    writer = csv.writer(response)
    writer.writerow(csv_headers)

    items = Item.objects.all().values(*fields)
    for item in items:
        if "active" in fields:
            item['active'] = "Active" if item["active"] == True else "Inactive"
        if "created_at" in fields:
            item['created_at'] = convert_to_localtime_str(item['created_at'])
        if "last_modified_at" in fields:
            item['last_modified_at'] = convert_to_localtime_str(item['last_modified_at'])

        writer.writerow(item.values())

    return writer

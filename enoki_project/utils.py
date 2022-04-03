def save_django_object(instance, data):
    '''
        Save a django object by attributing values to object's attribute.
    '''
    for key, value in data.items():
        setattr(instance, key, value)
    instance.save()

    return instance

def dictfetchall(cursor):
    '''
        Returns all rows from a cursor as a dict
    '''
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
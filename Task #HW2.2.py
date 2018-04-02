def select(*field_names):
    """This function allow to select from
    all field_names, names which you wanted
    """

    return lambda key: key in field_names


def field_filter(field_name,collection):
    """This function allow to filter all collection by
    field_names, wich you wanted
    """

    return lambda table: table[field_name] in collection

def query(table, select, *field_filters):
    """This function return filtred collection
    :param table - list of dictinaries which you wanted to fliter
    :type - list
    :param select - function, which allow to select
    :type - function
    :param - *field_filtres - filtres
    :type - function"""

    result = []
    for arg in table:
        if False not in map(lambda filter: filter(arg), field_filters):
            for key in arg.keys():
                if select(key):
                    result.append({key: arg[key]})
    return result
def data_from_module(data: dict):
    '''
    Reads dict and returns contents of "Module" field

    Parameters
    ----------
    data : dict
        AST of the module in dict format.
    '''
    if data.get('_type', '') == 'Module':
        return data.get('body', [])
    else:
        raise "Not a module" 
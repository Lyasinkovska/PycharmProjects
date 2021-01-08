search_actions = {'sn': ['firstname', None], 'sl': ['lastname', None],
                  'sf': ['fullname', None], 'snm': ['number', None],
                  'sc': ['city', None]}

if __name__ == '__main__':
    keys = [item[0] for item in search_actions.values()]
    print(keys)
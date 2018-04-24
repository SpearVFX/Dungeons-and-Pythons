def accepts(*types):
    def accepter(func):
        def check_arguments(*args):
            if len(types) != len(args):
                raise ValueError("Number of arguments in the decorator\
                                 and in the called function do not match.\n")

            for curr_type, curr_argument in zip(types, args):
                if type(curr_argument) is not curr_type:
                    raise TypeError(f'Argument {curr_argument}'
                                    f' is of type {type(curr_argument)}'
                                    f' expected type {curr_type}.\n')
            return func(*args)
        return check_arguments
    return accepter
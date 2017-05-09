
def get_method_name(displayname):
    return displayname[:displayname.index('(')]

def get_method_named_args_def(displayname):
    args = displayname[displayname.index('('):]

    if len(args) == 2:
        return args

    arg_index = 0
    index = 1
    previous_index = 1
    result = '('
    while index != -1:
        index = args.find(',', index)

        template_index = args.find('<', previous_index, index)

        if template_index != -1:
            index = args.find('>', template_index)
            index = args.find(',', index)

        if index == -1:
            break

        result += args[previous_index:index]
        result += " " + chr(ord('a') + arg_index) + ","
        index += 1
        previous_index = index
        arg_index += 1

    index = args.find(')', index)

    # Real type needs complete path (ex: 'const typename ::std::vector<_Tp, _Alloc>::value_type' for 'value_type')
    # So let's use c++14 auto deduction
    #result += args[previous_index:index] 
    result += "auto"

    result += " " + chr(ord('a') + arg_index) + ')'

    return result

def get_method_call(displayname):
    args = displayname[displayname.index('('):]

    if len(args) == 2:
        return displayname

    count = args.count(',') + 1

    result = get_method_name(displayname) + '('
    for i in range(0, count):
        result += chr(ord('a') + i)
        if i != count - 1:
            result += ', '
    result += ')'

    return result


def get_without_template(input):
    result = input
    template_index = input.find('<')
    if template_index != -1:
        #end_index = input.find('>', template_index)
        result = input[:template_index]

    return result

def snake_to_camel_case(input_str):
    tokens = input_str.split('::')
    result = ""
    first_token = True
    for token in tokens:
        if not first_token:
            result += "::"
        first_token = False
        words = token.split('_')
        first = True
        for word in words:
            result += word[:1] if first else word[:1].upper()
            result += word[1:]
            first = False
    return result

def snake_to_pascal_case(input_str):
    tokens = input_str.split('::')
    result = ""
    first_token = True
    for token in tokens:
        if not first_token:
            result += "::"
        first_token = False
        words = token.split('_')
        result = ""
        for word in words:
            result += word[:1].upper()
            result += word[1:]
    return result

__begin_id = "### BEGIN TEMPLATE:{id} ###"
__end_id = "### END TEMPLATE:{id} ###"


def process_file(path, **args):
    lines = []
    with open(path, "r") as file:
        write = True
        for line in file.readlines():
            if __get_starting_matching_item(line, args):
                lines.append(line)
                write = False
            if __get_ending_matching_item(line, args):
                write = True
            if write:
                lines.append(line)

    with open(path, "w+") as file:
        for line in lines:
            file.write(line)
            mod_lines = __get_starting_matching_item(line, args)
            if mod_lines:
                for mod_line in mod_lines:
                    file.write(mod_line + "\n")


def __get_starting_matching_item(line, args):
    for k in args.keys():
        if __begin_id.format(id=k) in line:
            return args[k]

    return None


def __get_ending_matching_item(line, args):
    for k in args.keys():
        if __end_id.format(id=k) in line:
            return args[k]

    return None

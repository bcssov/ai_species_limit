import vars

template = "asl_options_{0} = {{\n\tpotential = {{\n\t\tcheck_variable = {{\n\t\t\twhich = asl_allowed_species\n\t\t\tvalue = {0}\n\t\t}}\n\t}}\n\tallow = {{\n\t\talways = yes\n\t}}\n\teffect = {{\n\t}}\n}}"

for i in range(1, 21):
    print(template.format(str(i)))
import vars

template = " asl_counter_{0}:0 \"{0}\""

for i in range(1, vars.total):
    print(template.format(str(i)))
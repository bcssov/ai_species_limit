import vars

template = """
asl_options_{0} = {{
	potential = {{
		check_variable = {{
			which = asl_allowed_species
			value = {0}
		}}
	}}
	allow = {{
		always = yes
	}}
	effect = {{
	}}
}}"""

for i in range(1, 21):
    print(template.format(str(i)))
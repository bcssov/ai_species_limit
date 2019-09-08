from templates.utils import settings, templater

template = """
asl_options_{count} = {{
	potential = {{
		check_variable = {{
			which = asl_allowed_species
			value = {count}
		}}
	}}
	allow = {{
		always = yes
	}}
	effect = {{
	}}
}}"""


def process(publish_dir):
    lines = []
    for i in range(1, settings.total):
        lines.append(template.format(count=i))
    templater.process_file(
        publish_dir + "/common/button_effects/asl_button_effects.txt", effects=lines)

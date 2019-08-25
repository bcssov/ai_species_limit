from templates.utils import settings, templater

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


def process(publish_dir):
    lines = []
    for i in range(1, settings.total):
        lines.append(template.format(str(i)))
    templater.process_file(
        publish_dir + "/common/button_effects/asl_button_effects.txt", lines)

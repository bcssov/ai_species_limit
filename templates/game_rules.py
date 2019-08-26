from templates.utils import settings, templater

template = """
                {0} = {{
                    limit = {{
                        check_variable = {{
                            which = asl_allowed_species
                            value = {1}
                        }}
                    }}
                    count_exact_species = {{
                        count < {1}
                        limit = {{
                            OR = {{
                                is_same_species = prevprev
                                is_subspecies = prevprev
                            }}
                        }}
                    }}
                }}"""


def process(publish_dir):
    lines = []
    for i in range(1, settings.total):
        if i == 1:
            lines.append(template.format("if", i))
        else:
            lines.append(template.format("else_if", i))
    templater.process_file(
        publish_dir + "/common/game_rules/asl_rules.txt", lines)

from templates.utils import settings, templater

template = """
                {if_statement} = {{
                    limit = {{
                        check_variable = {{
                            which = asl_allowed_species
                            value = {count}
                        }}
                    }}
                    count_exact_species = {{
                        count < {count}
                        limit = {{
                            OR = {{
                                is_same_species = prevprevprev
                                is_subspecies = prevprevprev
                            }}
                        }}
                    }}
                }}"""


def process(publish_dir):
    lines = []
    for i in range(1, settings.total):
        if i == 1:
            lines.append(template.format(if_statement="if", count=i))
        else:
            lines.append(template.format(if_statement="else_if", count=i))
    templater.process_file(
        publish_dir + "/common/game_rules/asl_rules.txt", rules=lines)

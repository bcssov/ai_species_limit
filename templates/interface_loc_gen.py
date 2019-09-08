from templates.utils import settings, templater


template = ' asl_counter_{count}:0 "{count}"'


def process(publish_dir):
    lines = []
    for i in range(2, settings.total):
        lines.append(template.format(count=i))
    templater.process_file(
        publish_dir + "/localisation/english/asl_localization_l_english.yml", localisation=lines)

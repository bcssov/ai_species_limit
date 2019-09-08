from templates.utils import settings, templater

template = '''
        effectButtonType = {{
            name = "counter_{count}"
            quadTextureSprite = "GFX_asl_text_button"
            position = {{ x = 25 y = 300 }}
            size = {{ x = 40 y = 20 }}
            buttonFont = "cg_16b"
            buttonText = "asl_counter_{count}"
            clicksound = no_sound
            oversound = no_sound
            effect = "asl_options_{count}"
        }}'''


def process(publish_dir):
    lines = []
    for i in range(1, settings.total):
        lines.append(template.format(count=i))
    templater.process_file(
        publish_dir + "/interface/asl_options.gui", buttons=lines)

import vars

template = '''
        effectButtonType = {{
            name = "counter_{0}"
            quadTextureSprite = "GFX_asl_text_button"
            position = {{ x = 25 y = 300 }}
            size = {{ x = 40 y = 20 }}
            buttonFont = "cg_16b"
            buttonText = "asl_counter_{0}"
            clicksound = no_sound
            oversound = no_sound
            effect = "asl_options_{0}"
        }}'''

for i in range (1, vars.total):
    print(template.format(str(i)))

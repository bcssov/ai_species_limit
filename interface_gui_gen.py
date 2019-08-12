import vars

template = "\t\teffectButtonType = {{\n\t\t\tname = \"counter_{0}\"\n\t\t\tquadTextureSprite = \"GFX_asl_text_button\"\n\t\t\tposition = {{ x = 50 y = 230 }}\n\t\t\tbuttonFont = \"cg_16b\"\n\t\t\tbuttonText = \"asl_counter_{0}\"\n\t\t\tclicksound = no_sound\n\t\t\toversound = no_sound\n\t\t\teffect = \"asl_options_{0}\"\n\t\t}}"

for i in range (1, vars.total):
    print(template.format(str(i)))

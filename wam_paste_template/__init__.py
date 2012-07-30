from paste.script import templates

class CLI_Template(templates.Template):
    egg_plugins = ['wam_paste_cli_template']
    summary = 'Template for creating a CLI for wam'
    required_templates = []   # ['basic_package']
    _template_dir = 'cli_templates'
    # use_cheetah = True
    vars = [
    	templates.var('synapsis', 'One line synapsis of the tool', default='a tool to do something'),
    ]

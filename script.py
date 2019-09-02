from jinja2 import Environment
from jinja2 import FileSystemLoader

j2_env=Environment(loader=FileSystemLoader('templates'), trim_blocks=True)

template=j2_env.get_template("temp.j2")

rendered_file= template.render(name="Mario", event='e3')

print(rendered_file)

from pathlib import Path

import requests
import yaml
from jinja2 import Template


def inject_widgets(widgets: dict) -> dict:
    copy = widgets.copy()
    for idx, widget in enumerate(widgets):
        res = requests.get(widget["snippet"]["raw"])
        top, bottom = (int(line) for line in widget["snippet"]["lines"].split("-"))
        widget["snippet"] = "\n".join(res.text.split("\n")[top - 1 : bottom])
        copy[idx] = widget["snippet"]
    return widgets


if __name__ == "__main__":
    with Path("README.md.jinja2").open("r") as f:
        template = Template(f.read())

    with Path("awesome-textual.yml").open("r") as f:
        data = yaml.safe_load(f)

    data["widgets"] = inject_widgets(data["widgets"])
    output = template.render(apps=data["apps"], widgets=data["widgets"])

    with Path("README.md").open("w") as f:
        f.write(output)

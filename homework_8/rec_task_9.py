def render_template(template, context):
    tag = template.get("tag", "")
    attrs = template.get("attrs", {})
    content = template.get("content", "")
    children = template.get("children", [])

    attr_str = ""
    if attrs:
        attr_str = " " + " ".join(f'{key}="{value}"' for key, value in attrs.items())

    if isinstance(content, str):
        for key, value in context.items():
            placeholder = "{{ " + key + " }}"
            content = content.replace(placeholder, str(value))

    rendered_children = ""
    for child in children:
        rendered_children += render_template(child, context)

    if content:
        inner_html = content
    else:
        inner_html = rendered_children

    return f"<{tag}{attr_str}>{inner_html}</{tag}>"

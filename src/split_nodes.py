from textnode import Textnode, text_type_text, text_type_bold, text_type_italic, text_type_code


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(Textnode(sections[i], text_type_text))
            else:
                split_nodes.append(Textnode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

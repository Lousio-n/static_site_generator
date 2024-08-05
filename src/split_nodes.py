from textnode import Textnode, text_type_text, text_type_bold, text_type_italic, text_type_code


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            split_nodes.append(node)
            continue
        node_chars = []
        node_chars.extend(node.text)
        char_list = []
        delimiter_state = False

        if text_type == text_type_bold:
            for i in range(len(node_chars)):
                if "".join(node_chars[i:i+2]) == delimiter:
                    if delimiter_state:
                        split_nodes.append(
                            Textnode("".join(char_list), text_type_bold))
                        char_list.clear()
                        delimiter_state = not delimiter_state
                        continue
                    delimiter_state = not delimiter_state
                    split_nodes.append(
                        Textnode("".join(char_list), text_type_text))
                    char_list.clear()
                    continue
                if node_chars[i] != "*":
                    char_list.append(node_chars[i])
            if char_list:
                split_nodes.append(
                    Textnode("".join(char_list), text_type_text))
            continue

        for char in node_chars:
            if char == delimiter:
                if delimiter_state:
                    split_nodes.append(Textnode("".join(char_list), text_type))
                    char_list.clear()
                    delimiter_state = not delimiter_state
                    continue
                delimiter_state = not delimiter_state
                split_nodes.append(
                    Textnode("".join(char_list), text_type_text))
                char_list.clear()
                continue
            char_list.append(char)
        if char_list:
            split_nodes.append(Textnode("".join(char_list), text_type_text))

        if delimiter_state:
            raise Exception(
                "Markdown syntax error: unable to find closing delimiter")
    return split_nodes

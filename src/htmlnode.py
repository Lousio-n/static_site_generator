class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method is not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        html = ""
        for key, value in self.props.items():
            html += f' {key}="{value}"'
        return html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Error: must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.props}"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Error: tag missing")
        if self.children is None:
            raise ValueError("Error: parentnode must have children")

        def child_nodes_to_html(lst):
            html_string = ""
            for item in lst:
                if not isinstance(item, list):
                    html_string += item.to_html()
                else:
                    html_string += child_nodes_to_html(item)
            return f"<{self.tag}{self.props_to_html()}>{html_string}</{self.tag}>"
        return child_nodes_to_html(self.children)

    def __repr__(self):
        return f"{self.tag}, children: {self.children}, {self.props}"

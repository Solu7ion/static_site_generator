from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue
        
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid Markdown syntax for delimiter {delimiter}")
       
        for i, part in enumerate(parts):
            if i % 2 == 0:
                new_nodes.append(TextNode(part, "text"))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes

def generalStyle(elem: list, style: dict): # Sets a general style for table elements. e.g. thead, tbody, tr, td
    """
    parameters:

    elem -> list: table elements that should be drawn in this style
    style -> dict: A dictionary of this style's properties(key) and values(value)
    """

    style_ = ""
    elem_ = ""

    if len(style) < 1:
        return ""
    else:
        for key in style:
            style_ += key + ": " + style[key] + "; "
        
        for e in range(len(elem)):
            elem_ += elem[e]
            if (e != len(elem) - 1):
                elem_ += ", "
        
        return elem_ + " { " + style_ + "}"
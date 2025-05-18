from enum import Enum


class HTMLTag(Enum):
    HEADING_1 = "h1"
    HEADING_2 = "h2"
    HEADING_3 = "h3"
    HEADING_4 = "h4"
    HEADING_5 = "h5"
    HEADING_6 = "h6"
    PARAGRAPH = "p"
    BOLD = "b"
    ITALIC = "i"
    LINK = "a"
    IMAGE = "img"
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"
    LIST_ITEM = "li"
    BLOCKQUOTE = "blockquote"
    CODE = "code"


class HTMLNode:
    def __init__(
        self,
        tag: HTMLTag | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props is None:
            return ""

        return "".join([f' {key}="{value}"' for key, value in self.props.items()])

    def __eq__(self, other) -> bool:
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

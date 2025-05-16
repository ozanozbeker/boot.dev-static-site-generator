from textnode import TextNode, TextType


def main():
    textnode = TextNode("asdf", TextType.BOLD, "https://example.com")
    print(textnode)


main()

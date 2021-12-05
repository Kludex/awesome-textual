<!--lint disable double-link-->

# Awesome Textual | [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome)

> A curated list of awesome things related to [Textual](https://github.com/willmcgugan/textual).

[Textual](https://github.com/willmcgugan/textual) is a TUI (Text User Interface) framework for Python inspired by modern web development.

**To contribute, create an issue first. I'm still organizing the project. :pray:**

## Contents

- [Code Sharing](#code)
    - [Applications](#applications)
    - [Widgets](#widgets)
- [Resources](#resources)
    - [Tutorials](#tutorials)
    - [Videos](#videos)

## Code Sharing


### Applications

<details>
<summary><b><a href="https://github.com/chelnak/jenkins-tui/">Jenkins-tui</a></b> - Terminal based user interface for Jenkins. </summary>
<p>


![image info](https://raw.githubusercontent.com/chelnak/jenkins-tui/main/media/home_view.png "Jenkins-tui")


</p>
</details>


<details>
<summary><b><a href="https://github.com/sauljabin/kaskade">kaskade</a></b> - Terminal based user interface for kafka. </summary>
<p>


![image info](https://raw.githubusercontent.com/sauljabin/kaskade/main/screenshots/dashboard.png "kaskade")


</p>
</details>


<details>
<summary><b><a href="https://github.com/chelnak/textual-experiments">AutoCompleter</a></b> - A simple autocompleter for the terminal. </summary>
<p>



</p>
</details>



### Widgets

<details>
<summary><b><a href="https://github.com/chelnak/textual-experiments">FlitTextWidget</a></b> - A widget that will generate and display figlet text. </summary>
<p>




```python
class FigletTextWidget(Widget):
    """A widget that will generate and display figlet text."""

    has_focus = Reactive(False)
    mouse_over: bool = Reactive(False)

    def __init__(
        self,
        text: str,
        name: Optional[str] = None,
        style: Optional[Style] = None,
        layout_size: int = 8,
    ) -> None:
        """A widget that will generate and display figlet text.

        Args:
            text (str, optional): The text that will be rendered in the widget.
            name (str, optional): The name of the widget. Defaults to the name of the class.
            style (Style, optional): The style of the widget.
            layout_size (int, optional): The size of the widget. Defaults to 10.
        """

        super().__init__(name=name or self.__class__.__name__)
        self.text = text
        self.layout_size = layout_size
        self.style = style

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def on_focus(self) -> None:
        self.has_focus = True

    def on_blur(self) -> None:
        self.has_focus = False

    def render(self) -> RenderableType:

        return Align.center(
            renderable=FigletTextRenderable(text=self.text),
            vertical="middle",
            style=self.style or "",
            pad=False,
        )
```

</p>
</details>



## License

This project is under the MIT License.

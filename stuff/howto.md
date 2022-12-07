# Tips & Tricks

## How to do mermaid diagrams

Open VSCode and install the extension [Markdown Preview Mermaid Support](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)

Create a new file, ex: `mermaid.md` then you can write mermaid diagrams in your markdown file like this:

    ``` mermaid
    graph TD;
        A(Which way!?)-->B(Left);
        A-->C(Right);
        B-->D(It's a trap!);
        C-->D;
    ```

And it will render like this:

``` mermaid
graph TD;
    A(Which way!?)-->B(Left);
    A-->C(Right);
    B-->D(It's a trap!);
    C-->D;
```

More info on [mermaid website.](https://mermaid-js.github.io/mermaid/#/)

---

## Fun Diagrams

``` mermaid
graph TD
A[Good morning sunshine] --> B[Chech Github & Trello]
B --> C
C --> D[Take a deep breath]
D --> E[Start coding]
E --> F[Commit and push]
F --> G[Coffee break]
G --> C[Open VS Code]
```

---

Back to [Frontpage](../README.md)

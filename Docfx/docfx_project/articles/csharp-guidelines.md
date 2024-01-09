# C# Guidelines
## General
- Use four spaces of indentation (no tabs!)
- Avoid `this`, unless necessary
- Use async/await for any operations that include I/O (e.g reading/writing to a disk, database/network calls, etc)

## Validation
- Use FluentValidation to guard client input (e.g on API's)
- Use built-in argument checks for all method parameters

## Commenting
- Use XML comments on all classes and public methods
- Don't use comments for obvious logic

## Code Snippet
- Add code snippet by using this command

```markdown
[!code-csharp[] (../src/calculator.cs#L8-L13)]
```

- The result is as follows:

[!code-csharp[] (../src/calculator.cs#L8-L13)]

## Images
- Image can be added using this command

```markdown
![<alt-text>](../images/image_syntax.png)
```
- The result is as follows:

![<alt-text>](../images/image_syntax.png)

## Alerts

Alerts are block quotes that render with colors and icons that indicate the significance of the content.

The following alert types are supported:

```markdown
> [!NOTE]
> Information the user should notice even if skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]
> Essential information required for user success.

> [!CAUTION]
> Negative potential consequences of an action.

> [!WARNING]
> Dangerous certain consequences of an action.
```

They look like this in rendered page:

> [!NOTE]
> Information the user should notice even if skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]
> Essential information required for user success.

> [!CAUTION]
> Negative potential consequences of an action.

> [!WARNING]
> Dangerous certain consequences of an action.
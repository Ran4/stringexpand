A tiny python module for expanding strings.

## Usage:

```python3
>>> from stringexpand import expand
>>> expand("from_{x,y}_to_{a,b}")
['from_x_to_a', 'from_x_to_b', 'from_y_to_a', 'from_y_to_b']
>>> expand("file.{txt,pdf}")
['file.txt', 'file.pdf']
```

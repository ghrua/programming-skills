&#x1F3B9; **Run Command Line Using Python**

[Reference](https://stackoverflow.com/a/4760517/5793660)

```python
import subprocess
result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
print(result.stdout.decode("utf-8"))
```

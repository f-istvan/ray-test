ray test
========

Dockerized test run of the basic [ray](https://pypi.org/project/ray/) sample:

```python
def f():
    time.sleep(1)
    return 1
```

### Docker Build and Run 

```bash
docker build -t raytest . && docker run --rm -it raytest
```

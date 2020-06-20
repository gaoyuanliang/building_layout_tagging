## Using

### Test case 1

let's download a building layout image

```bash
wget https://www.crismatec.com/python/of/office-building-floor-plans-beautiful-design-layout-plan_office-decoration.jpg
```

this image looks like 

![](https://www.crismatec.com/python/of/office-building-floor-plans-beautiful-design-layout-plan_office-decoration.jpg)


then open you python3, and import the tagger

```python
from building_layout_tagging import building_layout_tagging
```

and run the tagging program 

```python
building_layout_tagging('office-building-floor-plans-beautiful-design-layout-plan_office-decoration.jpg')
```

you will the output:


```python
{'tag': 'building_layout', 'score': 0.99993956}
```

### Test case 2

let's dowload another image which looks like building layout but actually it is not

```bash
wget https://digitalcommunications.wp.st-andrews.ac.uk/files/2017/02/track-changes-example-1.png
```

this image looks like 

![](https://digitalcommunications.wp.st-andrews.ac.uk/files/2017/02/track-changes-example-1.png)

run my tagger against it

```python
building_layout_tagging('track-changes-example-1.png')
```

and the program says

```python
{'tag': 'non_building_layout', 'score': 0.6236702}
```

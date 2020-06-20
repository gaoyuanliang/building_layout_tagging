let's download a building layout image

```bash
wget https://www.crismatec.com/python/of/office-building-floor-plans-beautiful-design-layout-plan_office-decoration.jpg
```

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

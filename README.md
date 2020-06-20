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

let's dowload another image which looks like building layout but actually it is not

```bash
wget https://tr4.cbsistatic.com/hub/i/r/2017/06/16/e1cbfd87-4d4c-4f96-afa1-136c39e2985d/resize/1200x/b2fd39b21d2343264426b9bb5a2eee3d/wordtablelistd.jpg
```

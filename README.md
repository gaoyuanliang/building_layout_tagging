# Building layout tagging

This deep learning model tags the images of building layout, like

<table>
  <thead>
    <tr>
      <th>Input</th>
      <th>Output</th>
    </tr>
  </thead>
  <tr>
    <td>
      <img src="https://i.stack.imgur.com/s6yBz.jpg" width="600">
    </td>
    <td>
      <pre>
{
  'tag': 'building_layout', 
  'score': 0.99993956
}
</pre>
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://digitalcommunications.wp.st-andrews.ac.uk/files/2017/02/track-changes-example-1.png" width="600">
    </td>
    <td>
      <pre>
{
  'tag': 'non_building_layout', 
  'score': 0.6236702
}
</pre>
    </td>
  </tr>
</table>


## Installation


to install the building layout tagger, you need Python 3.7.7 

```bash
git clone https://github.com/liang6261515/building_layout_tagging.git

cd building_layout_tagging

pip3 install -r requirements.txt

wget https://github.com/fchollet/deep-learning-models/releases/download/v0.4/xception_weights_tf_dim_ordering_tf_kernels_notop.h5
```

download the pretrain model of cheque detection from this url [https://drive.google.com/file/d/1JPrSCBMQAzmY8rSvNgMt76fbv2tpuga3/view?usp=sharing](https://drive.google.com/file/d/1JPrSCBMQAzmY8rSvNgMt76fbv2tpuga3/view?usp=sharing) to the folder building_layout_tagging


## Using

### Test case 1

let's download a building layout image

```bash
wget https://www.crismatec.com/python/of/office-building-floor-plans-beautiful-design-layout-plan_office-decoration.jpg
```

this image looks like 

<img src="https://i.stack.imgur.com/s6yBz.jpg" width="600">

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

<img src="https://digitalcommunications.wp.st-andrews.ac.uk/files/2017/02/track-changes-example-1.png" width="600">

run my tagger against it

```python
building_layout_tagging('track-changes-example-1.png')
```

and the program says

```python
{'tag': 'non_building_layout', 'score': 0.6236702}
```

## I am looking for a job

feel free to contact me if you have any problem with this package or you are hiring data scientist/AI engineer. I am actively looking for data science/AI related jobs

My email: yanliang2345@outlook.com

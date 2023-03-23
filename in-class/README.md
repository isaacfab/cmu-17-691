## Use the notebook and data in this folder with docker to complete the in class exercise

launch the docker containter from your working directory with:

```
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work jupyter/datascience-notebook:2023-02-28
```
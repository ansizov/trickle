# Trickle

`Trickle` help us build `GitLab CI` projects. 
We have a lot of microservices and write them in one language. 
So all our `.gitlab-ci.yaml` are equal. 
This project get some arguments by http and build 
`yaml` template for microservice. We use Jinja2 as template engine.

## Example

Add `example.yaml` in `templates` folder:

```yaml
build_application {{ data.PROJECT_PATH }}:
  stage: build
  script:
    - cd {{ data.PROJECT_PATH }}
    - echo "You can build your project"

build_image {{ data.PROJECT_PATH }}:
  stage: build
  script:
    - cd {{ data.PROJECT_PATH }}
    - echo "Build {% if 'ARG' in data %}  with {% else %} without {% endif %} ARG"
```

Run project:

```bash
$ pip install -r requirements.txt
$ flask run
```

Get templates:

```bash
curl http://127.0.0.1:5000/?template=example.yaml
curl http://127.0.0.1:5000/?PROJECT_PATH=project1\&template=example.yaml
curl http://127.0.0.1:5000/?PROJECT_PATH=project2\&ARG=1\&template=example.yaml
```

## TODO

- Add yaml validator
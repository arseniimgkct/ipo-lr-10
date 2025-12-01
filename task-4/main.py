import json
from jinja2 import Template

data = json.load(open("data.json"))

template = Template('''
<html>
<head>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
<h1>Repositories</h1>  
<p>Источник: <a href="https://github.com/trending">Github Trending</a></p>                  
<table>
    <tbody>
    {% for repo in data %}
        <tr>
            <td>{{ repo.name }}</td>
            <td>{{ repo.stars }}</td>
        </tr>
    {% endfor %}
    </tbody>
</table>
'''
)

html = template.render(data=data)
open("index.html", "w+").write(html)
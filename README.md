# Tornado + Template + Improved Redirect
[![Python Version](https://img.shields.io/badge/python-3.7.4-green)](https://www.python.org/)
[![Tornado Version](https://img.shields.io/badge/tornado-6.0.3-green)](https://www.tornadoweb.org/en/stable/)

## Description

[Tornado](https://github.com/tornadoweb/tornado) is a powefull and lightweight python framework. BUT tornado haven't any template so you must start your project from scratch also tornado haven't post redirection(redirection with parameter(s) in post method). now these features are available!


- See also [Tornado-utilities](https://gitlab.com/reganto/tornado-utilities)

## Directory Structure

    tornado/
        handlers/
            home.py
            base.py
        logconfig/
        media/
            css/
                vendor/
            js/
                vendor/
            images/
        requirements/
            common.txt
            dev.txt
            production.txt
        templates/
            assets/
                base.html
                hide.html
            home/
                index.html
        vendor/
        environment.py
        fabfile.py
        app.py
        settings.py


## How to

First install Tornado

    pip install tornado

* It it better to install Tornado in virtualenv

* You should already install git

Clone repository to your local disk.

    git clone https://gitlab.com/reganto/tornado

Go to tornado directory.

Run this command in bash:

    sudo ./configure.sh

Now you can create a new project with this command:

    tornado project-name

Go to project directory.

For run server type this command in bash:

    python app.py --port=favorite-port  

* If you want to use post redirection:

  Your class must inherite from `BaseHandler`

```python
    from handlers.base import BaseHandler
```

in class method use `self.redirect_with_input()`


## Contributing

If you have improvements or bug fixes:

* Fork the repository on ~~GitHub~~ GitLab
* File an issue for the bug fix/feature request in ~~GitHub~~ GitLab
* Create a topic branch
* Push your modifications to that branch
* Send a pull request

## Authors

* [Reganto Blog](http://www.reganto.blog.ir)
* [Reganto GitLab](https://gitlab.com/reganto/)


> Everything Should Be Made as Simple as Possible, But Not Simpler

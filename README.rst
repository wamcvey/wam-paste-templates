wam-paste-templates
===================

A set of templates for 'paster create' that wam finds useful.


To Install
----------
Simply install (ideally into a virtualenv) simply download and then run:

   $ setup.py install

This should install the templates, as well as the `paster` utility
needed to evaluate the templates. You should be able to confirm
that the new template(s) are available using:

    $ paster create --list-templates
    Available templates:
      basic_package:  A basic setuptools-enabled package
      paste_deploy:   A web application deployed through paste.deploy
      wam_cli:        Template for creating a CLI for wam

Note the 'wam_cli' template. 

To Use
------
Once installed, using the template is simple:

    $ paster create -t wam_cli SomeProject
    Selected and implied templates:
      wam-paste-template#wam_cli  Template for creating a CLI for wam

    Variables:
      egg:      SomeProject
      package:  someproject
      project:  SomeProject
    Enter synapsis (One line synapsis of the tool) ['a tool to do something']: tool does something
    Creating template wam_cli
      Copying +project+.py_tmpl to ./SomeProject/SomeProject.py

In the directory `SomeProject` you should now have an expanded template CLI program.

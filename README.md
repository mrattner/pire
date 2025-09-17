# Pire

> **pire** _adj_ (plus mauvais)

A template for creating front-end projects in TypeScript with [Vite][1], made
using [cookiecutter][2]. It's called 'pire' to continue with Vite's French theme
and because I don't like JavaScript (c'est le pire).

## Prerequisites

### Cookiecutter

Install the [cookiecutter][3] application to be able to use the template.
Requires Python.

### NodeJS

You must have a working installation of NodeJS on your computer. If you are on
a POSIX-like system, the easiest way to install Node is via [`fnm`][4], the Fast
Node Manager. The package repositories for Node in APM, etc. tend to be very out
of date, so using a Node version manager is far preferable to installing Node
via other means.

## Using the template

Provide the URL to the Git repository to create a templated project in the
current directory:

```sh
cookiecutter gh:mrattner/pire
```

Follow the prompts, or press ENTER to accept the default values. Install the
JavaScript dependencies by running `npm install` in the project directory.

[1]: https://vite.dev/guide/cli.html
[2]: http://cookiecutter.readthedocs.io/en/latest/usage.html
[3]: http://cookiecutter.readthedocs.io/en/latest/installation.html
[4]: https://github.com/Schniz/fnm

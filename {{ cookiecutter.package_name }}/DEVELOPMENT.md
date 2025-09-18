# {{ cookiecutter.project_name }} Development guide

## Using Vite

Run `npm start` in the project directory to start a local development server on
port 5173 that will refresh automatically and report `tsc` compiler errors.

See [Vite config][viteconfig] for information about the `vite.config.js` file
and the [Vite features guide][vite] for more information and pitfalls to avoid.

### Lint, format, and type checking

Type-checking with typescript-eslint is enabled. This makes linting slower, so
you may need to [troubleshoot][tseslintperf] slow lint performance.

The following ESLint plugins are included:

- [`typescript-eslint`][tseslint] - Type-aware rules for more advanced linting
- [`@eslint-react/eslint-plugin`][eslintreact] - Replaces the default
  `eslint-plugin-react` and `eslint-plugin-react-hooks`. See notes about
  [migrating][eslintreactfaq] to ESLint React.
- [`eslint-plugin-react-refresh`][eslintrefresh] - Included by default
- [`eslint-plugin-import`][eslintimport] - Rules for consistent import/export
  statements
- [`eslint-plugin-jsx-a11y`][eslinta11y] - Rules for accessibility in JSX
  components
{%- if cookiecutter.add_tests|lower == "y" %}
- [`@vitest/eslint-plugin`][eslintvitest] and
  [`eslint-plugin-testing-library`][eslintrtl] - Rules for proper usage of
  Vitest and React Testing Library
{%- endif %}

[`eslint-config-prettier`][eslintpretty] is also included to turn off ESLint
rules that could conflict with Prettier. (Formatting is a different concern from
linting.)

Vite is primarily a bundler, not a file watcher. There are plugins for hooking
tools such as ESLint and stylelint into the auto-refreshing dev server, but you
should be using editor integration or an external filewatcher instead for such
tasks, in combination with the `format` and `lint` NPM scripts.
{%- if cookiecutter.add_tests|lower == "y" %}

### Running tests

Testing the components is done via [React Testing Library][rtl]. See [Vitest's
documentation][vitestdocs] and an [example][vitestrtl] of how to use
Vitest with React Testing Library.
{%- endif %}

## Components and styles

The design framework for the app is [Bulma][bulma]. Add the appropriate classes
to your semantic HTML elements to apply Bulma's themed element styles & layout.
{%- if cookiecutter.use_bulma_with_sass|lower == "y" %}
To customize the styling, modify the Sass files in the `public/styles` folder.
See [Bulma customization][bsass] for details.

Vite will compile the Sass to CSS as part of its build process.
{%- endif %}
{%- if cookiecutter.use_rtk_query|lower == "y" %}

## API integration

Integration with your backend API is via React Toolkit's [RTK-Query][rtk], using
auto-generated interfaces with the [openapi-typescript][oapi] CLI tool. Input
your OpenAPI specification
Recommended format for your backend API objects is based on [JSON:API][jsonapi].
{%- endif %}

[viteconfig]: https://vite.dev/config/
[vite]: https://vite.dev/guide/features
[tseslintperf]: https://typescript-eslint.io/troubleshooting/typed-linting/performance
[tseslint]: https://typescript-eslint.io/rules
[eslintreact]: https://eslint-react.xyz/docs/rules/overview
[eslintreactfaq]: https://eslint-react.xyz/docs/faq
[eslintrefresh]: https://github.com/ArnaudBarre/eslint-plugin-react-refresh/tree/main?tab=readme-ov-file#usage
[eslintimport]: https://github.com/import-js/eslint-plugin-import?tab=readme-ov-file#rules
[eslinta11y]: https://github.com/jsx-eslint/eslint-plugin-jsx-a11y?tab=readme-ov-file#supported-rules
[eslintpretty]: https://github.com/prettier/eslint-config-prettier?tab=readme-ov-file#eslintconfigjs-flat-config-plugin-caveat
[bulma]: https://bulma.io/documentation/elements/
{%- if cookiecutter.use_bulma_with_sass|lower == "y" %}
[bsass]: https://bulma.io/documentation/customize/with-sass/
{%- endif %}
{%- if cookiecutter.add_tests|lower == "y" %}
[eslintvitest]: https://github.com/vitest-dev/eslint-plugin-vitest?tab=readme-ov-file#rules
[eslintrtl]: https://github.com/testing-library/eslint-plugin-testing-library?tab=readme-ov-file#supported-rules
[rtl]: https://testing-library.com/docs/ecosystem-jest-dom/
[vitestdocs]: https://vitest.dev/api/
[vitestrtl]: https://www.robinwieruch.de/vitest-react-testing-library/
{%- endif %}
{%- if cookiecutter.use_rtk_query|lower == "y" %}
[rtk]: https://redux-toolkit.js.org/rtk-query/overview
[oapi]: https://www.npmjs.com/package/openapi-typescript
[jsonapi]: https://jsonapi.org/
{%- endif %}

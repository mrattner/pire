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

[`eslint-config-prettier`][eslintpretty] is also included to turn off ESLint
rules that could conflict with Prettier. (Formatting is a different concern from
linting.)

Vite is primarily a bundler, not a file watcher. There are plugins for hooking
tools such as ESLint and stylelint into the auto-refreshing dev server, but you
should be using editor integration or an external filewatcher instead for such
tasks, in combination with the `format` and `lint` NPM scripts.

## Components and styles

The design framework for the app is [Bulma][bulma]. Add the appropriate classes
to your semantic HTML elements to apply Bulma's themed element styles & layout.

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

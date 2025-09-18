import { render } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

/**
 * @see https://testing-library.com/docs/user-event/intro
 */
function setup(jsx) {
  return {
    user: userEvent.setup(),
    ...render(jsx),
  };
}

import { setup } from './test-utils';
import { screen } from '@testing-library/react';

import App from './App';

describe('App', () => {
  it('increments count when button clicked', async () => {
    const { user } = setup(<App />);

    await user.click(screen.getByRole('button'));
    await user.click(screen.getByRole('button'));

    expect(screen.getByRole('button')).toHaveTextContent('count is 2');
  });
});

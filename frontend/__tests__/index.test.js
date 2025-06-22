import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import Home from '../pages/index';
import '@testing-library/jest-dom';
import axios from 'axios';

jest.mock('axios'); // ✅ Mock Axios

describe('Frontend Page', () => {
  beforeEach(() => {
    axios.get.mockImplementation((url) => {
      if (url.includes('/api/health')) {
        return Promise.resolve({ data: { status: 'healthy' } });
      }
      if (url.includes('/api/message')) {
        return Promise.resolve({
          data: { message: "You've successfully integrated the backend!" },
        });
      }
      return Promise.reject(new Error('Unknown API call'));
    });
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  test('renders heading', () => {
    render(<Home />);
    const heading = screen.getByText(/DevOps Assignment/i);
    expect(heading).toBeInTheDocument();
  });

  test('fetches and displays backend message', async () => {
    render(<Home />);
    const message = await waitFor(() =>
      screen.getByText(/You've successfully integrated the backend!/i)
    );
    expect(message).toBeInTheDocument();
  });
});

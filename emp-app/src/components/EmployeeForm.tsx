import { useState } from 'react';
import { type Employee } from '../types/Employee';
import { createEmployee } from '../services/api';

interface Props {
  /** Callback to refresh employee list after a new employee is created */
  onEmployeeCreated: () => void;
}

/**
 * EmployeeForm Component
 *
 * A controlled form for employee-create creating new employees.
 * - Captures employee details (first name, last name, email, title, role, etc.)
 * - Sends data to the backend API using `createEmployee`.
 * - Displays success or error messages.
 *
 * @component
 * @param {Props} props - Component props
 * @returns {JSX.Element} Employee form UI
 */
const EmployeeForm: React.FC<Props> = ({ onEmployeeCreated }) => {
  /** Form state (excluding auto-generated ID field) */
  const [formData, setFormData] = useState<Omit<Employee, 'id'>>({
    first_name: '',
    last_name: '',
    email: '',
    title: '',
    role: '',
    employee_number: 0,
    organisation: '',
  });

  /** Loading state for API call */
  const [loading, setLoading] = useState<boolean>(false);

  /** Success message shown after employee is created */
  const [message, setMessage] = useState<string | null>(null);

  /** Error message shown if API request fails */
  const [error, setError] = useState<string | null>(null);

  /**
   * Handles input changes for form fields.
   * Converts `employee_number` input to a number before updating state.
   *
   * @param e - Input change event
   */
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: name === 'employee_number' ? Number(value) : value,
    }));
  };

  /**
   * Handles form submission:
   * - Prevents default reload
   * - Calls API to create new employee
   * - Resets form and triggers parent refresh on success
   * - Displays error message on failure
   *
   * @param e - Form submit event
   */
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setMessage(null);

    try {
      const response = await createEmployee(formData);
      setMessage(response);
      setFormData({
        first_name: '',
        last_name: '',
        email: '',
        title: '',
        role: '',
        employee_number: 0,
        organisation: '',
      });
      onEmployeeCreated(); // Refresh employee list
    } catch (err: any) {
      setError(
        err.response?.data?.detail || 'Failed to create employee. Check email or employee number.'
      );
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ margin: '20px 0', padding: '16px', border: '1px solid #ccc', borderRadius: '8px' }}>
      <h2>Add New Employee</h2>
      {message && <p style={{ color: 'green' }}>{message}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      <form onSubmit={handleSubmit}>
        {/* First Name */}
        <div style={{ marginBottom: '10px' }}>
          <label>
            First Name:
            <input
              type="text"
              name="first_name"
              value={formData.first_name}
              onChange={handleChange}
              required
              style={{ marginLeft: '8px', padding: '4px' }}
            />
          </label>
        </div>

        {/* Last Name */}
        <div style={{ marginBottom: '10px' }}>
          <label>
            Last Name:
            <input
              type="text"
              name="last_name"
              value={formData.last_name}
              onChange={handleChange}
              required
              style={{ marginLeft: '8px', padding: '4px' }}
            />
          </label>
        </div>

        {/* Email */}
        <div style={{ marginBottom: '10px' }}>
          <label>
            Email:
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
              style={{ marginLeft: '8px', padding: '4px' }}
            />
          </label>
        </div>

        {/* Title */}
        <div style={{ marginBottom: '10px' }}>
          <label>
            Title:
            <input
              type="text"
              name="title"
              value={formData.title}
              onChange={handleChange}
              required
              style={{ marginLeft: '8px', padding: '4px' }}
            />
          </label>
        </div>

        {/* Role */}
        <div style={{ marginBottom: '10px' }}>
          <label>
            Role:
            <input
              type="text"
              name="role"
              value={formData.role}
              onChange={handleChange}
              required
              style={{ marginLeft: '8px', padding: '4px' }}
            />
          </label>
        </div>

        {/* Employee Number */}
        <div style={{ marginBottom: '10px' }}>
          <label>
            Employee Number:
            <input
              type="number"
              name="employee_number"
              value={formData.employee_number || ''}
              onChange={handleChange}
              required
              style={{ marginLeft: '8px', padding: '4px' }}
            />
          </label>
        </div>

        {/* Organisation */}
        <div style={{ marginBottom: '10px' }}>
          <label>
            Organisation:
            <input
              type="text"
              name="organisation"
              value={formData.organisation}
              onChange={handleChange}
              required
              style={{ marginLeft: '8px', padding: '4px' }}
            />
          </label>
        </div>

        <button type="submit" disabled={loading}>
          {loading ? 'Creating...' : 'Create Employee'}
        </button>
      </form>
    </div>
  );
};

export default EmployeeForm;

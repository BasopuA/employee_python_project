import { useEffect, useState } from 'react';
import { type Employee } from '../types/Employee';
import { fetchEmployees } from '../services/api';

interface EmployeeListProps {
  /**
   * Optional trigger to refetch employees (e.g., after create/delete).
   * Increment this value to refresh the list.
   */
  refreshTrigger?: number;
}

const EmployeeList: React.FC<EmployeeListProps> = ({ refreshTrigger = 0 }) => {
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadEmployees = async () => {
      setLoading(true);
      try {
        const data = await fetchEmployees();
        setEmployees(data);
        setError(null); // Clear previous errors
      } catch (err) {
        console.error('Error fetching employees:', err);
        setError('Failed to load employees. Please try again later.');
        setEmployees([]);
      } finally {
        setLoading(false);
      }
    };

    loadEmployees();
  }, [refreshTrigger]); // Re-fetch whenever refreshTrigger changes

  if (loading) {
    return <p style={{ color: '#555' }}>Loading employee records...</p>;
  }

  if (error) {
    return <p style={{ color: 'red' }}>{error}</p>;
  }

  if (employees.length === 0) {
    return <p>No employees found. Please add one.</p>;
  }

  return (
    <div style={{ overflowX: 'auto', marginTop: '10px' }}>
      <table
        style={{
          width: '100%',
          borderCollapse: 'collapse',
          backgroundColor: '#fff',
          boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
          borderRadius: '8px',
          overflow: 'hidden',
        }}
      >
        <thead>
          <tr style={{ backgroundColor: '#1b4ad7ff', color: '#ecf0f1' }}>
            <th style={tableHeaderStyle}>ID</th>
            <th style={tableHeaderStyle}>Name</th>
            <th style={tableHeaderStyle}>Email</th>
            <th style={tableHeaderStyle}>Title</th>
            <th style={tableHeaderStyle}>Role</th>
            <th style={tableHeaderStyle}>Employee No.</th>
            <th style={tableHeaderStyle}>Organisation</th>
          </tr>
        </thead>
        <tbody>
          {employees.map((emp) => (
            <tr
              key={emp.id}
              style={{
                borderBottom: '1px solid #ddd',
                transition: 'background-color 0.2s',
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.backgroundColor = '#f8f9fa';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.backgroundColor = 'white';
              }}
            >
              <td style={tableCellStyle}>{emp.id}</td>
              <td style={tableCellStyle}>
                {emp.first_name} {emp.last_name}
              </td>
              <td style={tableCellStyle}>
                <a
                  href={`mailto:${emp.email}`}
                  style={{ color: '#3498db', textDecoration: 'none' }}
                >
                  {emp.email}
                </a>
              </td>
              <td style={tableCellStyle}>{emp.title}</td>
              <td style={tableCellStyle}>{emp.role}</td>
              <td style={tableCellStyle}>{emp.employee_number}</td>
              <td style={tableCellStyle}>{emp.organisation}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

// Reusable inline styles
const tableHeaderStyle: React.CSSProperties = {
  padding: '12px 10px',
  textAlign: 'left',
  fontWeight: 'bold',
  fontSize: '14px',
};

const tableCellStyle: React.CSSProperties = {
  padding: '10px',
  fontSize: '14px',
  color: '#333',
  borderTop: '1px solid #eee',
};

export default EmployeeList;
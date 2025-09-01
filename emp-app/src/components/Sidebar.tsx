import { Link } from 'react-router-dom';

const Sidebar: React.FC = () => {
  return (
    <aside
      style={{
        width: '250px',
        backgroundColor: '#1b4ad7ff',
        color: '#ecf0f1',
        padding: '20px 0',
        height: '100%',
        boxSizing: 'border-box',
      }}
    >
      <h2 style={{ textAlign: 'center', marginBottom: '30px', color: '#ecf0f1' }}>Admin Panel</h2>
      <nav>
        <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
          <li style={{ padding: '12px 20px', borderBottom: '1px solid #34495e' }}>
            <Link
              to="/display-all"
              style={{
                color: '#ecf0f1',
                textDecoration: 'none',
                fontSize: '16px',
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
              }}
            >
              📋 Display All Employees
            </Link>
          </li>
          <li style={{ padding: '12px 20px', borderBottom: '1px solid #34495e' }}>
            <Link
              to="/create"
              style={{
                color: '#ecf0f1',
                textDecoration: 'none',
                fontSize: '16px',
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
              }}
            >
              ➕ Create New Employee
            </Link>
          </li>
          <li style={{ padding: '12px 20px', borderBottom: '1px solid #26ce3fff' }}>
            <Link
              to="/find"
              style={{
                color: '#bdc3c7',
                textDecoration: 'none',
                fontSize: '16px',
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
              }}
            >
              🔍 Find an Employee
            </Link>
          </li>
          <li style={{ padding: '12px 20px', borderBottom: '1px solid #34495e' }}>
            <Link
              to="/update"
              style={{
                color: '#bdc3c7',
                textDecoration: 'none',
                fontSize: '16px',
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
              }}
            >
              ✏️ Update Employee
            </Link>
          </li>
          <li style={{ padding: '12px 20px', borderBottom: '1px solid #34495e' }}>
            <Link
              to="/delete"
              style={{
                color: '#e74c3c',
                textDecoration: 'none',
                fontSize: '16px',
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
              }}
            >
              ❌ Delete Employee
            </Link>
          </li>
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;
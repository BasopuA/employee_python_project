import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import DisplayAllPage from './pages/DisplayAllPage';
import CreateEmployeePage from './pages/CreateEmployeePage';
import FindEmployeePage from './pages/FindEmployeePage';
import UpdateEmployeePage from './pages/UpdateEmployeePage';
import DeleteEmployeePage from './pages/DeleteEmployeePage';

function App() {
  return (
    <Router>
      <div style={{ display: 'flex', height: '100vh', fontFamily: 'Arial, sans-serif' }}>
        {/* Sidebar */}
        <Sidebar />

        {/* Main Content */}
        <main style={{
          flex: 1,
          padding: '20px',
          backgroundColor: '#f9f9fb',
          overflowY: 'auto' // Enable scrolling if content overflows
        }}>
          <Routes>
            <Route path="/display-all" element={<DisplayAllPage />} />
            <Route path="/create" element={<CreateEmployeePage />} />
            <Route path="/find" element={<FindEmployeePage />} />
            <Route path="/update" element={<UpdateEmployeePage />} />
            <Route path="/delete" element={<DeleteEmployeePage />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
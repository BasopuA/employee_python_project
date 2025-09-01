import EmployeeForm from '../components/EmployeeForm';

const CreateEmployeePage: React.FC = () => {
  const handleEmployeeCreated = () => {
    alert('Employee created successfully!');
    // Optionally trigger refresh in EmployeeList via context or callback
  };

  return (
    <div>
      <h1>Create New Employee</h1>
      <EmployeeForm onEmployeeCreated={handleEmployeeCreated} />
    </div>
  );
};

export default CreateEmployeePage;
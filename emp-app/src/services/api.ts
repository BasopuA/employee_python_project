import axios from 'axios';
import { type Employee } from '../types/Employee';
const API_BASE_URL = 'http://localhost:8000';

export const api = axios.create({
  baseURL: API_BASE_URL,
});

// Get all employees
export const fetchEmployees = async (): Promise<Employee[]> => {
  const response = await api.get<Employee[]>('/v1/employees/');
  return response.data;
};

// Create a new employee
export const createEmployee = async (employee: Omit<Employee, 'id'>): Promise<string> => {
  const response = await api.post<{ Message: string }>('/v1/employees/', employee);
  return response.data.Message;
};
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./Employee.sol";
import "./AcademicCredential.sol";

contract Repository{
    mapping (uint => address) public employees;
    uint private number_of_employees = 0;

    event EmployeeAdded(uint employee_id, address employee_address);
    event AcademicCredentialAdded(uint academic_credential_id, address academic_credential_address);
    event EmployeeUpdated(uint employee_id, string new_name, string new_birth_date);
    event AcademicCredentialUpdated(uint employee_id, uint academic_credential_id, string new_credential_type, string new_field_of_study, string new_institution_name);

    function addEmployee(string memory name, string memory birth_date) public{
        Employee employee = new Employee(number_of_employees, name, birth_date);
        employees[number_of_employees] = address(employee);
        emit EmployeeAdded(number_of_employees, address(employee));
        number_of_employees++;

    }

    function updateEmployee(uint employee_id, string memory new_name, string memory new_birth_date) public{
        require(employee_id < number_of_employees, "Employee does not exist!");
        Employee(employees[employee_id]).updateDetails(new_name, new_birth_date);
        emit EmployeeUpdated(employee_id, new_name, new_birth_date);
    }

    function addAcademicCredential(uint employee_id, string memory credential_type, string memory field_of_study, string memory institution_name) public {
        require(employee_id < number_of_employees, "Employee does not exist!");
        Employee employee = Employee(employees[employee_id]);
        uint number_of_academic_credentials = employee.getAcademicCredentialsCount();
        AcademicCredential new_academic_credential = new AcademicCredential(number_of_academic_credentials, employee_id, credential_type, field_of_study, institution_name);
        employee.addAcademicCredential(address(new_academic_credential));
        emit AcademicCredentialAdded(number_of_academic_credentials, address(new_academic_credential));
        
    }

    function updateAcademicCredential(uint employee_id, uint academic_credential_id, string memory new_credential_type, string memory new_field_of_study, string memory new_institution_name) public{
        require(employee_id < number_of_employees, "Employee does not exist!");
        Employee employee = Employee(employees[employee_id]);
        uint number_of_academic_credentials = employee.getAcademicCredentialsCount();
        require(academic_credential_id < number_of_academic_credentials, "Academic credential with the given id does not exist for that patient!");
        address[] memory academic_credentials_addresses = employee.getAcademicCredentials();
        AcademicCredential academic_credential = AcademicCredential(academic_credentials_addresses[academic_credential_id]);
        academic_credential.updateAcademicCredential(new_credential_type, new_field_of_study, new_institution_name);
        emit AcademicCredentialUpdated(employee_id, academic_credential_id, new_credential_type, new_field_of_study, new_institution_name);
    }

    function getEmployee(uint employee_id) public view returns (address) {
        require(employee_id < number_of_employees, "Employee does not exist!");
        return employees[employee_id];
    }

    function getAllAcademicRecordsOfEmployee(uint employee_id) public view returns (address[] memory){
        require(employee_id < number_of_employees, "Employee does not exist!");
        Employee empployee = Employee(employees[employee_id]);
        return empployee.getAcademicCredentials();
    }

    function getCertainAcademicCredentialOfEmployee(uint employee_id, uint academic_credential_id) public view returns (address) {
        require(employee_id < number_of_employees, "Employee does not exist!");
        Employee employee = Employee(employees[employee_id]);
        uint number_of_academic_credentials = employee.getAcademicCredentialsCount();
        require(academic_credential_id < number_of_academic_credentials, "Academic credential with the given id does not exist!");
        address[] memory academic_credential_addresses = employee.getAcademicCredentials();
        return academic_credential_addresses[academic_credential_id-1];
    }


}

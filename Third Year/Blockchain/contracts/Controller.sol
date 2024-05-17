// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./Repository.sol";

contract Controller {
    Repository public repository;
    event AcademicCredentialCreated(uint employee_id, uint academic_credential_id);

    constructor (Repository _repository){
        repository = _repository;
    }

    modifier notEmptyString(string memory str) {
        require(bytes(str).length > 0, "String must not be empty");
        _;
    }

    function addEmployee(string memory name, string memory birth_date) public notEmptyString(name) notEmptyString(birth_date) {
        repository.addEmployee(name, birth_date);
    }

    function updateEmployee(uint employee_id, string memory new_name, string memory new_birth_date) public notEmptyString(new_name) notEmptyString(new_birth_date){
        repository.updateEmployee(employee_id, new_name, new_birth_date);
    }

    function addAcademicCredential(uint employee_id, string memory credential_type, string memory field_of_study, string memory institution_name) public notEmptyString(credential_type) notEmptyString(field_of_study) notEmptyString(institution_name){
        repository.addAcademicCredential(employee_id, credential_type, field_of_study, institution_name);
        emit AcademicCredentialCreated(employee_id, repository.getAllAcademicRecordsOfEmployee(employee_id).length - 1);
    }

    function updateAcademicCredential(uint employee_id, uint academic_credential_id, string memory new_credential_type, string memory new_field_of_study, string memory new_institution_name) public notEmptyString(new_credential_type) notEmptyString(new_field_of_study) notEmptyString(new_institution_name){
        repository.updateAcademicCredential(employee_id, academic_credential_id, new_credential_type, new_field_of_study, new_institution_name);
    }
}

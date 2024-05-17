// SPDX-License-Identifier: MIT 
pragma solidity ^0.8.0;

contract AcademicCredential{
    uint public id;
    uint public employee_id;
    string public credential_type;
    string public field_of_study;
    string public institution_name;

    constructor(uint _id, uint _employee_id, string memory _credential_type, string memory _field_of_study, string memory _institution_name){
        id = _id;
        employee_id = _employee_id;
        credential_type = _credential_type;
        field_of_study = _field_of_study;
        institution_name = _institution_name;
    }

    function updateAcademicCredential(string memory _credential_type, string memory _field_of_study, string memory _institution_name) public{
        credential_type = _credential_type;
        field_of_study = _field_of_study;
        institution_name = _institution_name;
    }
}
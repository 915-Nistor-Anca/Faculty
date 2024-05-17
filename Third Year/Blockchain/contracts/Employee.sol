// SPDX-License-Identifier: MIT 
pragma solidity ^0.8.0;

contract Employee{
    uint public id;
    string public name;
    string public birth_date;
    address[] public academic_credentials;

    constructor(uint _id, string memory _name, string memory _birth_date){
        id = _id;
        name = _name;
        birth_date = _birth_date;
    }

    function addAcademicCredential(address academic_credential_addresss) public{
        academic_credentials.push(academic_credential_addresss);
    }

    function getAcademicCredentials() public view returns (address[] memory) {
        return academic_credentials;
    }

    function updateDetails(string memory _name, string memory _birth_date) public{
        name = _name;
        birth_date = _birth_date;
    }

    function getAcademicCredentialsCount() public view returns (uint) {
        return academic_credentials.length;
    }
}
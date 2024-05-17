const Employee = artifacts.require("Employee");
const AcademicCredential = artifacts.require("AcademicCredential");

module.exports = function(deployer) {
  deployer.deploy(Employee, 1, "John", "2002-05-01");
  deployer.deploy(AcademicCredential, 1, 1, "Degree", "Computer Science", "UBB");
};
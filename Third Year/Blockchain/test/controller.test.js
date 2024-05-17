const Controller = artifacts.require("Controller");
const Repository = artifacts.require("Repository");
const Employee = artifacts.require("Employee");
const AcademicCredential = artifacts.require("AcademicCredential");

contract("Controller", (accounts) => {
    let controller;
    let repository;
    const [admin, user1] = accounts;

    before(async () => {
        repository = await Repository.new();
        controller = await Controller.new(repository.address);
    });

    describe("Employee management", () => {
        it("should fail to add an employee with an empty name", async () => {
            try {
                await controller.addEmployee("", "1990-01-01", { from: admin });
                assert.fail("The transaction should have reverted.");
            } catch (error) {
                assert.include(error.message, "String must not be empty", "Error message did not include the correct reason.");
            }
        });

        it("should fail to add an employee with an empty birth date", async () => {
            try {
                await controller.addEmployee("John Doe", "", { from: admin });
                assert.fail("The transaction should have reverted.");
            } catch (error) {
                assert.include(error.message, "String must not be empty", "Error message did not include the correct reason.");
            }
        });

        it("should add an employee", async () => {
            await controller.addEmployee("John Doe", "1990-01-01", { from: admin });
            const employeeAddress = await repository.getEmployee(0);
            const employee = await Employee.at(employeeAddress);
            const name = await employee.name();
            const birthDate = await employee.birth_date();
            assert.equal(name, "John Doe", "Employee's name was not set correctly.");
            assert.equal(birthDate, "1990-01-01", "Employee's birth date was not set correctly.");
        });

        it("should update an existing employee's details", async () => {
            await controller.updateEmployee(0, "Jane Doe", "1980-01-01", { from: admin });
            const employeeAddress = await repository.getEmployee(0);
            const employee = await Employee.at(employeeAddress);
            const name = await employee.name();
            const birthDate = await employee.birth_date();
            assert.equal(name, "Jane Doe", "Employee's name was not updated correctly.");
            assert.equal(birthDate, "1980-01-01", "Employee's birth date was not updated correctly.");
        });
    });

    describe("Academic credential management", () => {
        before(async () => {
            await controller.addEmployee("John Doe", "1990-01-01", { from: admin });
        });

        it("should fail to add an academic credential with an empty credential type", async () => {
            try {
                await controller.addAcademicCredential(0, "", "Computer Science", "Harvard", { from: admin });
                assert.fail("The transaction should have reverted.");
            } catch (error) {
                assert.include(error.message, "String must not be empty", "Error message did not include the correct reason.");
            }
        });

        it("should fail to add an academic credential with an empty field of study", async () => {
            try {
                await controller.addAcademicCredential(0, "Bachelor's Degree", "", "Harvard", { from: admin });
                assert.fail("The transaction should have reverted.");
            } catch (error) {
                assert.include(error.message, "String must not be empty", "Error message did not include the correct reason.");
            }
        });

        it("should fail to add an academic credential with an empty institution name", async () => {
            try {
                await controller.addAcademicCredential(0, "Bachelor's Degree", "Computer Science", "", { from: admin });
                assert.fail("The transaction should have reverted.");
            } catch (error) {
                assert.include(error.message, "String must not be empty", "Error message did not include the correct reason.");
            }
        });

        it("should add an academic credential", async () => {
            await controller.addAcademicCredential(0, "Bachelor's Degree", "Computer Science", "Harvard", { from: admin });
            const records = await repository.getAllAcademicRecordsOfEmployee(0);
            assert.equal(records.length, 1, "Academic credential was not added correctly.");
            const recordAddress = records[0];
            const record = await AcademicCredential.at(recordAddress);
            const credentialType = await record.credential_type();
            const fieldOfStudy = await record.field_of_study();
            const institutionName = await record.institution_name();
            assert.equal(credentialType, "Bachelor's Degree", "Academic credential's type was not set correctly.");
            assert.equal(fieldOfStudy, "Computer Science", "Academic credential's field of study was not set correctly.");
            assert.equal(institutionName, "Harvard", "Academic credential's institution name was not set correctly.");
        });

        it("should update an existing academic credential", async () => {
            await controller.updateAcademicCredential(0, 0, "Master's Degree", "Data Science", "MIT", { from: admin });
            const records = await repository.getAllAcademicRecordsOfEmployee(0);
            const recordAddress = records[0];
            const record = await AcademicCredential.at(recordAddress);
            const credentialType = await record.credential_type();
            const fieldOfStudy = await record.field_of_study();
            const institutionName = await record.institution_name();
            assert.equal(credentialType, "Master's Degree", "Academic credential's type was not updated correctly.");
            assert.equal(fieldOfStudy, "Data Science", "Academic credential's field of study was not updated correctly.");
            assert.equal(institutionName, "MIT", "Academic credential's institution name was not updated correctly.");
        });
    });
});

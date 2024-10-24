Maven is build tool for java.
There are multiple phases in java build
1. validate
2. compile
3. test
4. package
5. Integration test
6. verify 
7. Install
8. deplay
## validate - validate the project is correct and all necessary information is available
## compile - compile the source code of the project
##  test - test the compiled source code using a suitable unit testing framework. These tests should not require the code be packaged or deployed
## package - take the compiled code and package it in its distributable format, such as a JAR.
##  verify - run any checks on results of integration tests to ensure quality criteria are met
## install - install the package into the local repository, for use as a dependency in other projects locally
##  deploy - done in the build environment, copies the final package to the remote repository for sharing with other developers and projects.
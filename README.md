# codebuild-runner
AWS Lambda function that runs a CodeBuild project

This function runs on any event passed to it and starts a build on the project specified by the environment variable `PROJECT_NAME`. Note that this function will return success if it is able to start the build, and does not wait for the build's finish.

## Environment Variables
* `PROJECT_NAME` - the CodeBuild project name to build
#!/usr/bin/env groovy

pipeline {
    agent none

    stages {
        stage('Validate') {
            agent {
                dockerfile {
                    additionalBuildArgs '--target lint'
                    filename 'Dockerfile'
                }
            }
            steps {
                sh 'python -m unittest discover -v tests'
                sh 'pylint --disable=C0111,C0301 --persistent=no --output-format=parseable lebanese_channels > pylint.out || exit 0'
            }
            post {
                always {
                    warnings canComputeNew: false, canResolveRelativePaths: false, canRunOnFailed: true, categoriesPattern: '', parserConfigurations: [[parserName: 'PyLint', pattern: 'pylint.out']], defaultEncoding: '', excludePattern: '', healthy: '', includePattern: '', messagesPattern: '', unHealthy: ''
                }
            }
        }
        stage('Deploy') {
            agent any
            when {
                branch 'master'
            }
            steps {
                sh 'rsync -Crv ./ /opt/channels/ --delete'
                sh 'sudo /bin/systemctl restart channels.service'
            }
        }
    }
}

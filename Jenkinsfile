properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
  stage("clone") {
    git branch: 'main', url: 'https://github.com/lubani/DevOps2412.git'
  }
  stage ("show files") {
    sh 'ls -l'
  }
}

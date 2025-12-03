pipeline {
    agent any

    stages {

        /* ------------------------------
           1️⃣ Run Selenium Tests (Manasa)
        --------------------------------*/
        stage('Run Selenium Tests with pytest') {
            steps {
                echo "Running Selenium Tests using pytest"

                // Install Python dependencies
                bat '"C:\\Users\\MANASA\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe" install -r requirements.txt'

                // Start Flask app non-blocking
                bat 'start "" "C:\\Users\\MANASA\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" app.py'

                // Wait for server to start
                bat 'ping 127.0.0.1 -n 5 > nul'

                // Run Selenium tests
                bat '"C:\\Users\\MANASA\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pytest -v'
            }
        }

        /* ------------------------------
           2️⃣ Build Docker Image (Manasa)
        --------------------------------*/
        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image..."
                bat 'docker build -t kubdemoapp:v1 .'
            }
        }

        /* ------------------------------
           3️⃣ Docker Login (Manasa)
        --------------------------------*/
        stage('Docker Login') {
            steps {
                echo "Logging into Docker Hub..."
                bat 'docker login -u varimallamansa1 -p "Manasa@247"'
            }
        }

        /* ------------------------------
           4️⃣ Push Docker Image to Docker Hub (Manasa)
        --------------------------------*/
        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Pushing Docker Image to Docker Hub..."
                bat 'docker tag kubdemoapp:v1 varimallamansa1/sample1:kubeimage1'
                bat 'docker push varimallamansa1/sample1:kubeimage1'
            }
        }

        /* ------------------------------
           5️⃣ Deploy to Kubernetes (Manasa)
        --------------------------------*/
        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes..."
                withEnv(['KUBECONFIG=C:\\Users\\MANASA\\.kube\\config']) {
                    bat 'kubectl apply -f deployment.yaml --validate=false'
                    bat 'kubectl apply -f service.yaml'
                }
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up Python processes...'
            bat 'taskkill /F /IM python.exe /T || exit 0'
        }
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Please check the logs.'
        }
    }
}

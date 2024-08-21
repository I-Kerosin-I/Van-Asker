function addQuestion() {
            const questionsContainer = document.getElementById('questions-container');
            const questionDiv = document.createElement('div');
            questionDiv.classList.add('question');

            questionDiv.innerHTML = `
                <label>Вопрос:</label>
                <input type="text" placeholder="Введите вопрос" required>
                <div>
                    <label for="multiple-choice">Несколько верных ответов:</label>
                    <input type="checkbox" id="multiple-choice">
                </div>
                <div class="answers-container"></div>
                <button class="button" onclick="addAnswer(this)">Добавить вариант ответа</button>
                <span class="remove-btn" onclick="removeQuestion(this)">Удалить вопрос</span>
            `;

            questionsContainer.appendChild(questionDiv);
        }

        function addAnswer(button) {
            const answersContainer = button.previousElementSibling;
            const answerDiv = document.createElement('div');
            answerDiv.classList.add('answer');

            answerDiv.innerHTML = `
                <input type="text" placeholder="Введите вариант ответа" required>
                <label for="correct-answer">Верный ответ:</label>
                <input type="checkbox" id="correct-answer">
                <span class="remove-btn" onclick="removeAnswer(this)">Удалить вариант</span>
            `;

            answersContainer.appendChild(answerDiv);
        }

        function removeQuestion(button) {
            const questionDiv = button.parentElement;
            questionDiv.remove();
        }

        function removeAnswer(button) {
            const answerDiv = button.parentElement;
            answerDiv.remove();
        }
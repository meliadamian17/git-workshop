// JavaScript Functionality
document.getElementById('add-btn').addEventListener('click', addTask);

function addTask() {
  const input = document.getElementById('todo-input');
  const taskText = input.value.trim();

  if (taskText !== "") {
    const listItem = document.createElement('li');
    listItem.textContent = taskText;

    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.onclick = () => listItem.remove();

    listItem.appendChild(deleteButton);
    document.getElementById("todo-list").appendChild(listItem);

    input.value = "";
  }
}

document
  .getElementById("todo-input")
  .addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
      addTask();
    }
  });

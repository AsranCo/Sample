//inMind
const inMindAddBtn = document.querySelector("#inMind .btn-add");
const inMindCancelBtn = document.querySelector("#inMind .btn-cancel");
const inMindSaveBtn = document.querySelector("#inMind .btn-save");
const inMindInput = document.querySelector("#inMind .form");
const inMindItemsBox = document.querySelector("#inMind .items-box");

//toDo
const toDoAddBtn = document.querySelector("#toDo .btn-add");
const toDoCancelBtn = document.querySelector("#toDo .btn-cancel");
const toDoSaveBtn = document.querySelector("#toDo .btn-save");
const toDoInput = document.querySelector("#toDo .form");
const toDoItemsBox = document.querySelector("#toDo .items-box");

//doing
const doingAddBtn = document.querySelector("#doing .btn-add");
const doingCancelBtn = document.querySelector("#doing .btn-cancel");
const doingSaveBtn = document.querySelector("#doing .btn-save");
const doingInput = document.querySelector("#doing .form");
const doingItemsBox = document.querySelector("#doing .items-box");

//done
const doneAddBtn = document.querySelector("#done .btn-add");
const doneCancelBtn = document.querySelector("#done .btn-cancel");
const doneSaveBtn = document.querySelector("#done .btn-save");
const doneInput = document.querySelector("#done .form");
const doneItemsBox = document.querySelector("#done .items-box");

//trash
const trash = document.querySelector(".trash");

let inMindArray = getDataLS().inMindArray;
let toDoArray = getDataLS().toDoArray;
let doingArray = getDataLS().doingArray;
let doneArray = getDataLS().doneArray;

inMindArray.forEach((item) => {
  createItem(item.value, "inMind", item.id);
});

toDoArray.forEach((item) => {
  createItem(item.value, "toDo", item.id);
});

doingArray.forEach((item) => {
  createItem(item.value, "doing", item.id);
});

doneArray.forEach((item) => {
  createItem(item.value, "done", item.id);
});

function getDataLS() {
  let inMindArray = [];
  let toDoArray = [];
  let doingArray = [];
  let doneArray = [];

  if (localStorage.getItem("kanban-inMind")) {
    inMindArray = JSON.parse(localStorage.getItem("kanban-inMind"));
  }
  if (localStorage.getItem("kanban-toDo")) {
    toDoArray = JSON.parse(localStorage.getItem("kanban-toDo"));
  }
  if (localStorage.getItem("kanban-doing")) {
    doingArray = JSON.parse(localStorage.getItem("kanban-doing"));
  }
  if (localStorage.getItem("kanban-done")) {
    doneArray = JSON.parse(localStorage.getItem("kanban-done"));
  }

  return { inMindArray, toDoArray, doingArray, doneArray };
}

function setDataLS() {
  const doneItems = document.querySelectorAll("#done .item");
  const doingItems = document.querySelectorAll("#doing .item");
  const toDoItems = document.querySelectorAll("#toDo .item");
  const inMindItems = document.querySelectorAll("#inMind .item");

  let inMindArray = [];
  let toDoArray = [];
  let doingArray = [];
  let doneArray = [];

  inMindItems.forEach((item) => {
    inMindArray.push({ value: item.textContent, id: item.id });
  });
  localStorage.setItem("kanban-inMind", JSON.stringify(inMindArray));

  toDoItems.forEach((item) => {
    toDoArray.push({ value: item.textContent, id: item.id });
  });
  localStorage.setItem("kanban-toDo", JSON.stringify(toDoArray));

  doingItems.forEach((item) => {
    doingArray.push({ value: item.textContent, id: item.id });
  });
  localStorage.setItem("kanban-doing", JSON.stringify(doingArray));

  doneItems.forEach((item) => {
    doneArray.push({ value: item.textContent, id: item.id });
  });
  localStorage.setItem("kanban-done", JSON.stringify(doneArray));
}

function showForm(id) {
  if (id === "inMind") {
    inMindInput.classList.remove("hide");
    inMindInput.focus();
    inMindSaveBtn.classList.remove("hide");
    inMindCancelBtn.classList.remove("hide");
    inMindAddBtn.classList.add("hide");
  } else if (id === "toDo") {
    toDoInput.classList.remove("hide");
    toDoInput.focus();
    toDoSaveBtn.classList.remove("hide");
    toDoCancelBtn.classList.remove("hide");
    toDoAddBtn.classList.add("hide");
  } else if (id === "doing") {
    doingInput.classList.remove("hide");
    doingInput.focus();
    doingSaveBtn.classList.remove("hide");
    doingCancelBtn.classList.remove("hide");
    doingAddBtn.classList.add("hide");
  } else if (id === "done") {
    doneInput.classList.remove("hide");
    doneInput.focus();
    doneSaveBtn.classList.remove("hide");
    doneCancelBtn.classList.remove("hide");
    doneAddBtn.classList.add("hide");
  }
}

function hideForm(id) {
  if (id === "inMind") {
    inMindInput.classList.add("hide");
    inMindSaveBtn.classList.add("hide");
    inMindCancelBtn.classList.add("hide");
    inMindAddBtn.classList.remove("hide");
  } else if (id === "toDo") {
    toDoInput.classList.add("hide");
    toDoSaveBtn.classList.add("hide");
    toDoCancelBtn.classList.add("hide");
    toDoAddBtn.classList.remove("hide");
  } else if (id === "doing") {
    doingInput.classList.add("hide");
    doingSaveBtn.classList.add("hide");
    doingCancelBtn.classList.add("hide");
    doingAddBtn.classList.remove("hide");
  } else if (id === "done") {
    doneInput.classList.add("hide");
    doneSaveBtn.classList.add("hide");
    doneCancelBtn.classList.add("hide");
    doneAddBtn.classList.remove("hide");
  }
}

function createItem(value, id, itemId = null) {
  const item = document.createElement("h4");
  item.textContent = value;
  item.className = "item";
  item.draggable = true;
  item.id = itemId || `${new Date().getTime()}${value}`;
  item.setAttribute("ondragstart", "dragstart(event)");
  item.setAttribute("ondragend", "dragend()");

  if (id === "inMind") {
    inMindItemsBox.appendChild(item);
  } else if (id === "toDo") {
    toDoItemsBox.appendChild(item);
  } else if (id === "doing") {
    doingItemsBox.appendChild(item);
  } else if (id === "done") {
    doneItemsBox.appendChild(item);
  }
}

function onPlusClick(id) {
  if (id === "inMind") {
    showForm("inMind");
    hideForm("toDo");
    hideForm("doing");
    hideForm("done");
  } else if (id === "toDo") {
    showForm("toDo");
    hideForm("inMind");
    hideForm("doing");
    hideForm("done");
  } else if (id === "doing") {
    showForm("doing");
    hideForm("toDo");
    hideForm("inMind");
    hideForm("done");
  } else if (id === "done") {
    showForm("done");
    hideForm("toDo");
    hideForm("doing");
    hideForm("inMind");
  }
}

function onSaveClick(id) {
  if (id === "inMind") {
    if (inMindInput.value !== "") {
      createItem(inMindInput.value, "inMind");
      inMindInput.value = "";
      hideForm("inMind");
    }
  } else if (id === "toDo") {
    if (toDoInput.value !== "") {
      createItem(toDoInput.value, "toDo");
      toDoInput.value = "";
      hideForm("toDo");
    }
  } else if (id === "doing") {
    if (doingInput.value !== "") {
      createItem(doingInput.value, "doing");
      doingInput.value = "";
      hideForm("doing");
    }
  } else if (id === "done") {
    if (doneInput.value !== "") {
      createItem(doneInput.value, "done");
      doneInput.value = "";
      hideForm("done");
    }
  }

  setDataLS();
}

inMindInput.addEventListener("keyup", function (event) {
  if (event.keyCode === 13) {
    onSaveClick("inMind");
  }
});

toDoInput.addEventListener("keyup", function (event) {
  if (event.keyCode === 13) {
    onSaveClick("toDo");
  }
});

doingInput.addEventListener("keyup", function (event) {
  if (event.keyCode === 13) {
    onSaveClick("doing");
  }
});

doneInput.addEventListener("keyup", function (event) {
  if (event.keyCode === 13) {
    onSaveClick("done");
  }
});

function dragstart(e) {
  e.dataTransfer.setData("text", e.target.id);
}

function dragend() {
  inMindItemsBox.classList.remove("active");
  toDoItemsBox.classList.remove("active");
  doingItemsBox.classList.remove("active");
  doneItemsBox.classList.remove("active");
  trash.classList.remove("active");
}

function allowDrop(e) {
  e.preventDefault();
  e.target.classList.add("active");
}

function drop(e) {
  e.preventDefault();
  let data = e.dataTransfer.getData("text");
  if (e.target.classList.contains("items-box")) {
    e.target.appendChild(document.getElementById(data));
  } else if (e.target.classList.contains("item")) {
    e.target.parentElement.appendChild(document.getElementById(data));
  }

  setDataLS();
}

function dropTrash(e) {
  e.preventDefault();
  let data = e.dataTransfer.getData("text");

  let inMindArray = getDataLS().inMindArray;
  let toDoArray = getDataLS().toDoArray;
  let doingArray = getDataLS().doingArray;
  let doneArray = getDataLS().doneArray;

  inMindItemsBox.innerHTML = "";
  toDoItemsBox.innerHTML = "";
  doingItemsBox.innerHTML = "";
  doneItemsBox.innerHTML = "";

  inMindArray.forEach((item) => {
    if (item.id !== data) {
      createItem(item.value, "inMind", item.id);
    }
  });

  toDoArray.forEach((item) => {
    if (item.id !== data) {
      createItem(item.value, "toDo", item.id);
    }
  });

  doingArray.forEach((item) => {
    if (item.id !== data) {
      createItem(item.value, "doing", item.id);
    }
  });

  doneArray.forEach((item) => {
    if (item.id !== data) {
      createItem(item.value, "done", item.id);
    }
  });

  setDataLS();
}

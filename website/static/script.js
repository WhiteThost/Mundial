const draggable_list = document.getElementById('draggable-list');

const listItems = [];

let dragStartIndex;

createList(GA_list, 0, 'A');
createList(GB_list, 1, 'B');
createList(GC_list, 2, 'C');
createList(GD_list, 3, 'D');
createList(GE_list, 4, 'E');
createList(GF_list, 5, 'F');
createList(GG_list, 6, 'G');
createList(GH_list, 7, 'H');

function createList(countries_list, group_n, group_l){
    const listItems_s = [];

    const group_title = document.createElement('h2')
    group_title.classList.add('group-title');
    group_title.innerHTML = `
      <h1 class="group-title">Group ${group_l}</h1>
      `
    draggable_list.appendChild(group_title);

    countries_list.forEach((country, index) => {
        const listItem = document.createElement('li')
        listItem.setAttribute('data-index', index);
        listItem.setAttribute('data-group', group_n);
        listItem.setAttribute('data-true_id', country[0]);
        listItem.innerHTML = `
          <span class="number">${index + 1}</span>
          <div class="draggable" draggable="true">
            <p class="country-name">${country[1]}</p>
            <img src="https://flagicons.lipis.dev/flags/4x3/${country[2]}.svg">
          </div>
          `;
      
        listItems_s.push(listItem);
        draggable_list.appendChild(listItem);
      });
    listItems[group_n] = listItems_s;

    addEventListeners(listItems);
}

function dragStart() {
  // console.log('Event: ', 'dragstart');
  dragStartIndex = +this.closest('li').getAttribute('data-index');
  dragStartGroup = +this.closest('li').getAttribute('data-group');
  dragStartId = +this.closest('li').getAttribute('data-true_id');
}

function dragEnter() {
  // console.log('Event: ', 'dragenter');
  this.classList.add('over');
}

function dragLeave() {
  // console.log('Event: ', 'dragleave');
  this.classList.remove('over');
}

function dragOver(e) {
  // console.log('Event: ', 'dragover');
  e.preventDefault();
}

function dragDrop() {
  // console.log('Event: ', 'drop');
 
  const dragEndIndex = +this.getAttribute('data-index');
  const dragEndGroup = +this.getAttribute('data-group');
  const dragEndId = +this.getAttribute('data-true_id');

  swapItems(dragStartIndex, dragEndIndex, dragStartGroup, dragEndGroup, dragStartId, dragEndId);
  this.classList.remove('over');
}

function swapItems(fromIndex, toIndex, fromGroup, toGroup, fromId, toId) {
  if (fromGroup === toGroup) {
  const itemOne = listItems[fromGroup][fromIndex].querySelector('.draggable');
  const itemTwo = listItems[toGroup][toIndex].querySelector('.draggable');
  listItems[fromGroup][fromIndex].setAttribute('data-true_id', toId)
  listItems[toGroup][toIndex].setAttribute('data-true_id', fromId)

  listItems[fromGroup][fromIndex].appendChild(itemTwo);
  listItems[toGroup][toIndex].appendChild(itemOne);
  
  listItems.forEach(item => {
    item.forEach(i => {
      console.log(i);
  })})
}
}

function addEventListeners() {
  const draggables = document.querySelectorAll('.draggable');
  const dragListItems = document.querySelectorAll('.draggable-list li');

  draggables.forEach(draggable => {
    draggable.addEventListener('dragstart', dragStart);
  });

  dragListItems.forEach(item => {
    item.addEventListener('dragover', dragOver);
    item.addEventListener('drop', dragDrop);
    item.addEventListener('dragenter', dragEnter);
    item.addEventListener('dragleave', dragLeave);
  });
}

function send_info(){
  const order = []
  listItems.forEach(item => {
    item.forEach(i => {
      console.log(i);
      var c_id = i.getAttribute('data-true_id');
      order.push(c_id);
    })
  });
  console.log(order);
  //const dict_value = {listItems: listItems};
  //const s = JSON.stringify(dict_value)
  fetch('/save_pickem', {
    method: 'POST',
    body: JSON.stringify(order),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  })
}

